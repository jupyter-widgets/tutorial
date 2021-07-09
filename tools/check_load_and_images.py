"""
Iterate through and execute all notebooks
"""
from collections import defaultdict
from pathlib import Path
import random
import re

from execute_notebooks import print_exceptions


def main():
    p = Path('.')
    notebook_paths = p.glob('**/*.ipynb')
    patterns = dict(
        loads=re.compile(r'%load ([^\s]+\.py)'),
        images=re.compile(r'\!\[.+\]\((.*images/[^\s]+(?:png|jpg|jpeg|svg))\)')
    )
    exceptions = defaultdict(list)

    for nb_path in notebook_paths:
        if '.ipynb_checkpoints' in str(nb_path):
            continue
        print(nb_path)
        with open(nb_path) as f:
            contents = f.read()
        for name, pattern in patterns.items():
            print(f'Checking {name}...')
            matches = pattern.findall(contents)
            for match in matches:
                print(f'\t{match}')
                p = nb_path.parent / match
                try:
                    with open(p) as _:
                        pass
                except FileNotFoundError as e:
                    exceptions[str(nb_path)].append(str(e))

    print_exceptions(exceptions)


if __name__ == '__main__':
    main()
