from __future__ import print_function

tutorial_name = 'Jupyter widget ecosystem'

requirements = [
    'ipywidgets',
    'bqplot',
    'ipyleaflet',
    'ipyvolume',
    'pythreejs',
    'ccdproc',
    'ginga'
]

import_result = {p: False for p in requirements}

print("Checking requirements for {}".format(tutorial_name))

for package in requirements:
    try:
        __import__(package)
        import_result[package] = True
    except ImportError:
        pass

success = all(import_result.values())

version_check_packages = {'ipywidgets': '7.0.0a11',
                          'bqplot': '0.10',
                          'ipyleaflet': '0.4',
                          'ipyvolume': '0.4'}


if success:
    print('All required packages installed')
else:
    print('Please install these missing packages '
          'for the tutorial "{}":'.format(tutorial_name))
    missing = [k for k, v in import_result.items() if not v]
    print('\t' + '\n\t'.join(missing))

print('Checking version numbers of these packages: ',
      ', '.join(version_check_packages.keys()))


def version_checker(package_name, version, nbextension=None):
    good_version = version.startswith(version_check_packages[package_name])
    if nbextension is None:
        nbextension = package_name
    if not good_version:
        print('\n**** Please upgrade {} to version {} by running:'.format(package_name,
                                                                          version_check_packages[package_name]))
        print('        conda remove --force {} # if you use conda'.format(package_name))
        print('        pip install --pre --upgrade {}'.format(package_name))
        print('        jupyter nbextension enable --py {}'.format(nbextension))
    else:
        print('\n{} version is good!'.format(package_name))


# Check as many packages as we can...


try:
    import ipywidgets
except ImportError:
    pass
else:
    ipywidgets_version = ipywidgets.__version__
    version_checker('ipywidgets', ipywidgets_version,
                    nbextension='widgetsnbextension')
try:
    import bqplot
except ImportError:
    pass
else:
    bqplot_version = bqplot.__version__
    version_checker('bqplot', bqplot_version)

try:
    import ipyleaflet
except ImportError:
    pass
else:
    ipyleaflet_version = ipyleaflet.__version__
    version_checker('ipyleaflet', ipyleaflet_version)

try:
    import ipyvolume
except ImportError:
    pass
else:
    ipyvolume_version = ipyvolume.__version__
    version_checker('ipyvolume', ipyvolume_version)
