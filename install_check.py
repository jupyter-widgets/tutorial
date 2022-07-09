import sys
import logging
from subprocess import check_call, CalledProcessError


SUCCESS_PREFIX = '🎉'
FIX_PREFIX = '⚠️⚠️⚠️ ----->'

tutorial_name = 'Jupyter widget ecosystem'

requirements = [
    'notebook',
    'ipywidgets',
    'bqplot',
    'ipyleaflet',
    'ipyvolume',
    'pythreejs',
    'ipytree',
    'ipydatagrid',
    'ipycytoscape',
    'ipygany',
    'jupyterlab',
    'voila',
    'pyvista',
    'mpl_interactions',
    'orjson',  # For one of the example in ipycanvas
]

import_result = {p: False for p in requirements}

print("Checking requirements for {}".format(tutorial_name), end='')

for package in requirements:
    try:
        __import__(package)
        import_result[package] = True
    except ImportError:
        pass
    print('.', end='', flush=True)

print()
success = all(import_result.values())

# List compatible versions for each package
version_check_packages = {'ipywidgets': ['7.7'],
                          'jupyterlab': ['3'],
                         }

if success:
    print(f'\t{SUCCESS_PREFIX} All required packages installed')
else:
    print(FIX_PREFIX, 'Please install these missing packages '
          'for the tutorial "{}":'.format(tutorial_name))
    missing = [k for k, v in import_result.items() if not v]
    print('\t' + '\n\t'.join(missing))

print('Checking voila version:')

try:
    check_call(['voila', '--version'])
    print(f'\t{SUCCESS_PREFIX} Voila is correctly installed')
except CalledProcessError:
    print(f'\t {FIX_PREFIX} Voila is not installed! Please install it by running one '
          'of the following:')
    print('        conda install -c conda-forge voila')
    print('        pip install voila')

print('Checking version numbers of these packages: ',
      ', '.join(version_check_packages.keys()))


def version_checker(package_name, version, nbextension=None):
    good_version = any(version.startswith(v) for
                       v in version_check_packages[package_name])
    if nbextension is None:
        nbextension = package_name
    if not good_version:
        newest = version_check_packages[package_name][-1]
        print('\n**** Please upgrade {} to version {} by running:'.format(package_name,
                                                                          newest))
        print('        conda install {}={} # if you use conda'.format(package_name, newest))
        print('        pip install {}=={}'.format(package_name, newest))
    else:
        print(f'\t{SUCCESS_PREFIX} {package_name} version is good!')


# Check as many packages as we can...


try:
    import ipywidgets
except ImportError:
    pass
else:
    ipywidgets_version = ipywidgets.__version__
    version_checker('ipywidgets', ipywidgets_version)

try:
    import jupyterlab
except ImportError:
    pass
else:
    jupyterlab_version = jupyterlab.__version__
    version_checker('jupyterlab', jupyterlab_version)

# Check that the appropriate kernel has been created

required_kernel = 'widgets-tutorial'

print('Checking whether kernel {} exists'.format(required_kernel))

import jupyter_client

known_kernels = list(jupyter_client.kernelspec.find_kernel_specs().keys())
if required_kernel not in known_kernels:
    print(FIX_PREFIX, 'Please create custom kernel with: ',
          'ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix')
else:
    print(f'\t{SUCCESS_PREFIX} Custom kernel is correctly installed')

# Check that lab extensions are installed

print('Checking whether all Jupyter lab extensions are installed')

lab_extensions = [
    '@jupyter-widgets/jupyterlab-manager',
    '@jupyter-widgets/jupyterlab-sidecar',
    'bqplot',
    'jupyter-threejs',
    'jupyter-leaflet',
    'ipyvolume',
    'ipytree',
    'ipycanvas',
    'ipydatagrid',
    'ipygany',
    'jupyter-cytoscape',  # for ipycytoscape
    'jupyter-matplotlib',
    'jupyter-vuetify',
]


try:
    from jupyterlab.commands import check_extension, AppOptions
    from jupyterlab_server.config import get_federated_extensions
except ImportError:
    print(FIX_PREFIX, 'Please install jupyterlab before checking extensions.')
else:
    missing_extensions = []

    # Fetch federated extensions
    federated_extensions = get_federated_extensions([sys.base_prefix + '/share/jupyter/labextensions']).keys()

    # JupyterLab be quiet
    logger = logging.Logger('quiet')
    logger.setLevel(logging.CRITICAL)
    app_options = AppOptions(logger=logger)

    for extension in lab_extensions:
        if not check_extension(extension, app_options=app_options) and extension not in federated_extensions:
            missing_extensions.append(extension)

    if missing_extensions:
        print(FIX_PREFIX, 'These lab extensions are missing: ',
              ', '.join(missing_extensions))
        print(FIX_PREFIX,' Please try to install the following packages with conda or pip: ',
              ', '.join(missing_extensions))
    else:
        print(f'\t{SUCCESS_PREFIX} All extensions are installed!')
