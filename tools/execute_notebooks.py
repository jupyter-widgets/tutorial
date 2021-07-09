"""
Iterate through and execute all notebooks
"""
from pathlib import Path

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor


def main():
    p = Path('.')
    notebook_paths = p.glob('**/*.ipynb')
    exceptions = {}
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
            exceptions[str(nb_path)] = e

    if exceptions:
        print('⚠️' * 20)
        print('\n\nFailures in these notebooks:')
        print('\n'.join(exceptions.keys()), '\n\n')
        print('⚠️' * 20)
        for nb, error in exceptions.items():
            print(f'{nb}: \n{error}')
    else:
        print('🎉🎉 Everything worked! 🎉🎉')


if __name__ == '__main__':
    main()
