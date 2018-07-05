import os
import re
from argparse import ArgumentParser

import nbformat

NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

NBVERSION = 4

REG = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')

NO_NUMBER = ['00']


def iter_notebooks(directory):
    return sorted(nb for nb in os.listdir(NOTEBOOK_DIR) if REG.match(nb))


def get_notebook_title(nb_file):
    nb = nbformat.read(os.path.join(NOTEBOOK_DIR, nb_file),
                       as_version=NBVERSION)
    for cell in nb.cells:
        if cell.source.startswith('# '):
            return cell.source[1:].splitlines()[0].strip()
    else:
        # Apparently there was no heading, raise an error
        raise ValueError('No title found for {}.'.format(nb_file))


def gen_contents(directory=None, path_prefix=None):
    for nb in iter_notebooks(directory):
        if path_prefix:
            nb_url = os.path.join(path_prefix, nb)
        else:
            nb_url = nb
        chapter, section, title = REG.match(nb).groups()
        title = get_notebook_title(nb)
        if section == '00':
            if chapter in NO_NUMBER:
                yield '\n### [{0}]({1})'.format(title, nb_url)
            else:
                yield '\n### [{0}. {1}]({2})'.format(int(chapter),
                                                     title, nb_url)
        else:
            yield "- [{0}]({1})".format(title, nb_url)


def contents(directory=None, path_prefix=None):
    """
    Generate the table of contents as a string.
    """
    return '\n'.join(gen_contents(directory))


def write_notebook(toc, filename, toc_name="Table of Contents"):
    notebook = nbformat.v4.new_notebook()
    toc_cell_contents = '\n'.join(['# {}'.format(toc_name), toc])
    toc_cell = nbformat.v4.new_markdown_cell(toc_cell_contents)
    notebook['cells'] = [toc_cell]
    nbformat.write(notebook, filename)


if __name__ == '__main__':
    parser = ArgumentParser(description='Generate a table of contents from a '
                                        'directory of notebooks')
    parser.add_argument('-o', '--output',
                        help='Destination for the table of contents. If the '
                             'extension is .ipynb then the output is a '
                             'Jupyter notebook, otherwise the content is '
                             'plain markdown. Default is to print to stdout.')
    parser.add_argument('-d', '--directory',
                        help='Directory containing the notebooks from which '
                             'to generate contents. Default value is '
                             '{}'.format(NOTEBOOK_DIR))
    parser.add_argument('-p', '--path-prefix',
                        help='If set, this string will be prepended to the '
                             'links to the notebook in the generated table '
                             'of contents.')
    args = parser.parse_args()
    directory = args.directory or NOTEBOOK_DIR
    toc = contents(directory, path_prefix=args.path_prefix)
    if not args.output:
        print(toc)
    elif args.output.endswith('.ipynb'):
        write_notebook(toc, args.output)
    else:
        with open(args.output, 'w') as f:
            f.write(toc)
    print('\n', 70 * '#', '\n')
