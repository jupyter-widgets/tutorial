import os
import re
from argparse import ArgumentParser

import nbformat

NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

NBVERSION = 4

REG = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')

NO_NUMBER = ['00']

TOC_STYLES = ['header_ulist', 'nested_list']


def iter_notebooks(directory):
    return sorted(nb for nb in os.listdir(NOTEBOOK_DIR) if REG.match(nb))


def is_title(cell):
    return cell.source.startswith('# ')


def get_notebook_title(nb_file):
    nb = nbformat.read(os.path.join(NOTEBOOK_DIR, nb_file),
                       as_version=NBVERSION)
    for cell in nb.cells:
        if is_title(cell):
            return cell.source[1:].splitlines()[0].strip()
    else:
        # Apparently there was no heading, raise an error
        raise ValueError('No title found for {}.'.format(nb_file))


def gen_contents(directory=None, path_prefix=None,
                 auto_number=False, toc_style=None):

    current_chapter = -1
    for nb in iter_notebooks(directory):
        if path_prefix:
            nb_url = os.path.join(path_prefix, nb)
        else:
            nb_url = nb
        chapter, section, title = REG.match(nb).groups()

        # Generate auto chapter and section numbers even if
        # we do not end up using them
        if chapter != current_chapter:
            current_chapter = chapter
            current_section = 1
        else:
            current_section += 1

        title = get_notebook_title(nb)

        # No spaces allowed in URLs...
        nb_url = nb_url.replace(' ', '%20')
        if section == '00':
            if toc_style == 'nested_list':
                yield f'{chapter}. [{title}]({nb_url})'
            else:
                if chapter in NO_NUMBER:
                    yield '\n### [{0}]({1})'.format(title, nb_url)
                else:
                    yield '\n### [{0}. {1}]({2})'.format(int(chapter),
                                                         title, nb_url)
        else:
            if toc_style == 'nested_list':
                yield f'    {section}. [{title}]({nb_url})'
            else:
                yield "- [{0}]({1})".format(title, nb_url)


def contents(directory=None, **kwd):
    """
    Generate the table of contents as a string.
    """
    return '\n'.join(gen_contents(directory, **kwd))


def write_notebook(toc, filename, toc_name="Table of Contents"):
    notebook = nbformat.v4.new_notebook()
    toc_cell_contents = '\n'.join(['# {}'.format(toc_name), toc])
    toc_cell = nbformat.v4.new_markdown_cell(toc_cell_contents)
    notebook['cells'] = [toc_cell]
    nbformat.write(notebook, filename)


if __name__ == '__main__':
    parser = ArgumentParser(description='Generate a table of contents from a '
                                        'directory of notebooks. The notebooks '
                                        'should be named so that when sorted '
                                        'by name they are in the order they '
                                        'should appear in the table of contents.')
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
    parser.add_argument('--auto-number', action='store_true',
                        help='Automatically number table of contents entries.')
    parser.add_argument('--toc-style', choices=TOC_STYLES,
                        default='nested_list',
                        help='Set the style for the table of contents.')
    args = parser.parse_args()
    directory = args.directory or NOTEBOOK_DIR
    toc = contents(directory, path_prefix=args.path_prefix,
                   auto_number=args.auto_number,
                   toc_style=args.toc_style)
    if not args.output:
        print(toc)
    elif args.output.endswith('.ipynb'):
        write_notebook(toc, args.output)
    else:
        with open(args.output, 'w') as f:
            f.write(toc)
    print('\n', 70 * '#', '\n')
