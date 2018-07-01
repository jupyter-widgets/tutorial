from argparse import ArgumentParser
from pathlib import Path

import nbformat

NB_VERSION = 4


def change_kernel_name(notebook_name, kernel_name, display_name=None):
    """
    Change the name of the notebook kernel.
    """
    dname = display_name if display_name else kernel_name
    notebook = nbformat.read(notebook_name, NB_VERSION)
    current_kname = notebook['metadata']['kernelspec']['name']
    current_dname = notebook['metadata']['kernelspec']['display_name']
    if current_kname == kernel_name and current_dname == dname:
        print('not changing kernel of {}'.format(notebook_name))
        return

    notebook['metadata']['kernelspec']['name'] = kernel_name
    notebook['metadata']['kernelspec']['display_name'] = dname
    # print('\nHad this been a real operation, would have changed {}'.format(notebook_name))
    # print('\t\tcurrent: {} to new: {}\n'.format(current_kname, kernel_name))
    nbformat.write(notebook, notebook_name)


def get_kernel_name(notebook_name):
    """
    Return the name of the kernel in the notebook.
    """
    notebook = nbformat.read(notebook_name, NB_VERSION)
    kname = notebook['metadata']['kernelspec']['name']
    return kname


if __name__ == '__main__':
    parser = ArgumentParser(description='Get or set kernel names for all '
                                        'notebooks in a directory.')
    parser.add_argument('-d', '--directory', default='.',
                        help='Directory in which to look for notebooks.')
    parser.add_argument('-s', '--set',
                        dest='kernel_name',
                        metavar='kernel_name',
                        help="Set the kernel to this name for each notebook.")
    parser.add_argument('--display-name',
                        help="Display name of the kernel (default is same as "
                             "kernel name).")

    args = parser.parse_args()

    directory = args.directory if args.directory else '.'
    p = Path(directory)
    notebooks = list(p.glob('**/*.ipynb'))

    if not notebooks:
        raise RuntimeError('No notebooks found at path {}'.format(directory))

    for notebook in notebooks:
        nb_str = str(notebook)
        if args.kernel_name:
            change_kernel_name(nb_str, args.kernel_name,
                               display_name=args.display_name)
        else:
            kname = get_kernel_name(nb_str)
            print('{}\t\t\t\t{}'.format(nb_str, kname))
