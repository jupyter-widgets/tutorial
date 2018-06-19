import re
import itertools
from pathlib import Path

import nbformat
from stdlib_list import stdlib_list

VALID_PACKAGE_CHARS = '[a-zA-Z0-9_]'
REG = re.compile(f'^\s*import ({VALID_PACKAGE_CHARS}+)|^\s*from ({VALID_PACKAGE_CHARS}+)\b+\simport', re.ASCII)


def import_statements(code_source):
    """
    Find and return all lines in the code cells of a notebook that contain
    import statements.

    Parameters
    ----------

    code_source : an nbformat NotebookNode object or str
        Notebook whose cells will be checked for import statements or the
        contents of a Python file  (as a string).

    Returns
    -------

    list
        List of strings, each an import statement from the notebook.
    """
    if isinstance(code_source, str):
        import_code = [code_source]
    else:
        import_cells = [c for c in code_source['cells'] if
                        c['cell_type'] == 'code' and 'import' in c['source']]
        import_code = [c['source'] for c in import_cells]

    imports = [line for code in import_code
               for line in code.split('\n') if REG.match(line)]

    return imports


def dependency_names_from_import_statements(imports, unique=True):
    """
    Extract the package names from a list of import statements.

    Parameters
    ----------

    imports : list
        List of import statements from which package names will be extracted.

    unique : bool, optional
        If ``True``, return list of unique package names, otherwise return
        package names in same order as input.
    """
    packages = []
    for i in imports:
        imp = REG.search(i)
        for g in imp.groups():
            if g is not None:
                packages.append(g)
                continue

    if unique:
        packages = list(set(packages))

    return packages


def bad_imports(imports, as_written=False):
    """
    Try a bunch of imports and report whether each was successful.

    Parameters
    ----------
    imports : list
        List of import statements (e.g. ``import numpy`` or
        ``from astropy import units``) to try. Leading whitespace in the
        imports list is fine; it will be stripped before trying the import.

    as_written : bool, optional
        If ``True``, test the import statements exactly as they are passed in.
        Otherwise, just test the package name (i.e. the top-level import).

    Returns
    -------

    list
        List of bool, ``True`` if the import fails, ``False`` if it succeeds.
    """

    result = []
    for imp in imports:
        if as_written:
            test = imp.strip()
        else:
            test = dependency_names_from_import_statements([imp])[0]
            test = 'import ' + test
        try:
            exec(test)
        except ModuleNotFoundError:
            result.append(True)
        else:
            result.append(False)

    return result


def identify_dependencies(directory, nb_version=4,
                          exclude_hidden=True, skip=None,
                          notebooks=True, python_files=True,
                          verbose=False):
    """
    Find all notebooks in or below a directory, grab their import
    statements, and translate that to a list of dependencies.

    Parameters
    ----------

    directory : str
        Path to directory to be searched for notebook. All subdirectories of
        this path will be searched.

    nb_version : int, optional
        Notebook version to assume when reading notebooks.

    exclude_hidden : bool, optional
        Exclude hidden directories or files (i.e. those whose name begins
        with ``.``).

    skip : list of str, optional
        List of notebook or directory names to skip. If a directory name is
        part of the list then all notebooks below that directory will be
        skipped. The name must match exactly to cause a skip.

    notebooks : bool, optional
        If ``True``, check for imports in notebooks.

    python_files : bool, optional
        If ``True``, check for imports in python files (i.e. files that
        end ``.py``).

    verbose: bool, optional
        If ``True``, print summary of progress while working.
    """
    p = Path(directory)

    notebook_paths = p.glob('**/*.ipynb') if notebooks else []
    python_paths = p.glob('**/*.py') if python_files else []

    dep_info = {
        'path': [],
        'imports': [],
        'packages': [],
        'missing': [],
    }

    for path in itertools.chain(notebook_paths, python_paths):
        # Skip any directories or files that start with a dot...
        hidden = [part.startswith('.') and part != '..' for part in path.parts]

        skips = any(part in skip for part in path.parts) if skip else False

        if any(hidden) or skips:
            if verbose:
                print(f'...Skipping {path}', path.parts[-1])
            continue

        if path.suffix == '.ipynb':
            nbnode = nbformat.read(str(path), nb_version)
        else:
            with path.open() as f:
                nbnode = f.read()
        imports = import_statements(nbnode)

        bads = bad_imports(imports)
        any_bad = any(bads)
        deps = dependency_names_from_import_statements(imports, unique=False)

        # print(f'Checked file { path } found { "SOME" if any_bad else "no" } bad imports')
        if any_bad:
            bad_list = [p for p, b in zip(deps, bads) if b]
            if verbose:
                print(f'    Missing packages: {bad_list}')

        dep_info['path'].extend([str(path)] * len(imports))
        dep_info['imports'].extend(imports)
        dep_info['packages'].extend(deps)
        dep_info['missing'].extend(bads)

    return dep_info


def packages_to_install(dep_info, exclude=None):
    """
    Produce a list of packages that need to be installed to use this set of
    materials. Python standard library modules are excluded.

    Parameters
    ----------

    dep_info : dict
        Dictionary of dependency information, generated by
        `identify_dependencies`.

    exclude : list, optional
        List of packages to exclude from the results.

    Returns
    -------

    list
        List of packages needed for whatever set of files this was run on.
    """

    if exclude is None:
        exclude = []

    packages = list(set(dep_info['packages']))
    standard = stdlib_list("3.6")

    packages = [p for p in packages if p not in standard and p not in exclude]
    return packages


if __name__ == '__main__':
    # Some day add options...
    directory = '.'
    dep_info = identify_dependencies(directory, skip=['setup.py'])
    to_install = packages_to_install(dep_info)
    print(' '.join(to_install))
