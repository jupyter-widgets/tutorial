"""
Iterate through and execute all notebooks
"""
from collections import defaultdict
from pathlib import Path
import random
import re


def main():
    p = Path('.')
    notebook_paths = p.glob('**/*.ipynb')
    patterns = dict(
        loads=re.compile(r'%load ([^\s]+\.py)'),
        images=re.compile(r'\((images/[^\s]+(?:png|jpg|jpeg))\)')
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

    if exceptions:
        print('⚠️' * 20)
        print('\n\nFailures in these notebooks:')
        print('\n'.join(exceptions.keys()), '\n\n')
        print('⚠️' * 20)
        for nb, error_list in exceptions.items():
            face = random.choice(["😮", "😱", "🤬"])
            print(face * 20)
            errors = "\n".join(error_list)
            print(f'{nb}: \n{errors}')
            print(face * 20)
    else:
        print('🎉🎉 Everything worked! 🎉🎉')


if __name__ == '__main__':
    main()
