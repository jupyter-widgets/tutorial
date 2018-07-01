from pathlib import Path

from tools.kernel_names import get_kernel_name

TUTORIAL_KERNEL_NAME = 'widget-tutorial'
NOTEBOOK_DIRECTORY = Path(__file__) / '..' / 'notebooks'


def test_kernel_name():
    notebooks = NOTEBOOK_DIRECTORY.glob('**/*.ipynb')
    for notebook in notebooks:
        kernel_name = get_kernel_name(str(notebook))
        assert kernel_name == TUTORIAL_KERNEL_NAME
