from __future__ import print_function

tutorial_name = 'Pure python widgets'

requirements = ['ipywidgets', 'bqplot', 'ipyleaflet', 'ipyvolume', 'pythreejs']

import_result = {p: False for p in requirements}

print("Checking requirements for {}".format(tutorial_name))

for package in requirements:
    try:
        __import__(package)
        import_result[package] = True
    except ImportError:
        pass

success = all(import_result.values())

if success:
    print('All required packages installed!')
else:
    print('Please install these packages '
          'for the tutorial "{}":'.format(tutorial_name))
    missing = [k for k, v in import_result.items() if not v]
    print('\t' + '\n\t'.join(missing))
