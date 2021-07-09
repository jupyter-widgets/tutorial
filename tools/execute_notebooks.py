"""
Iterate through and execute all notebooks
"""
from collections import defaultdict
from pathlib import Path
import random

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor


def print_exceptions(exceptions):
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


def main():
    p = Path('.')
    notebook_paths = p.glob('**/*.ipynb')
    exceptions = defaultdict(list)
    for nb_path in notebook_paths:
        if '.ipynb_checkpoints' in str(nb_path):
            continue
        print(nb_path)
        notebook = nbf.read(nb_path, 4)
        try:
            ep = ExecutePreprocessor()
            print('About to execute')
            ep.preprocess(notebook)
            print('Done executing')
        except Exception as e:
            exceptions[str(nb_path)].append(str(e))
    print_exceptions(exceptions)



if __name__ == '__main__':
    main()
