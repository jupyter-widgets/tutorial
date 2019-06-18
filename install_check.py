from subprocess import check_call, CalledProcessError


FIX_PREFIX = '----->'

tutorial_name = 'Jupyter widget ecosystem'

requirements = [
    'notebook',
    'ipywidgets',
    'bqplot',
    'ipyleaflet',
    'ipyvolume',
    'pythreejs',
    'ipyevents',
    'ipysheet',
    'ipytree',
    'pywwt',
    'jupyterlab'
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
version_check_packages = {'ipywidgets': ['7.4', '7.5'],
                          'notebook': ['5.7'],
                          'jupyterlab': ['0.35', '1.0']
                         }

if success:
    print('\tAll required packages installed')
else:
    print(FIX_PREFIX, 'Please install these missing packages '
          'for the tutorial "{}":'.format(tutorial_name))
    missing = [k for k, v in import_result.items() if not v]
    print('\t' + '\n\t'.join(missing))

print('Checking voila version:')

try:
    check_call(['voila', '--version'])
    print('\tVoila is correctly installed')
except CalledProcessError:
    print('\tVoila is not installed! Please install it by running one '
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
        print('\t{} version is good!'.format(package_name))


# Check as many packages as we can...


try:
    import ipywidgets
except ImportError:
    pass
else:
    ipywidgets_version = ipywidgets.__version__
    version_checker('ipywidgets', ipywidgets_version)

try:
    import notebook
except ImportError:
    pass
else:
    notebook_version = notebook.__version__
    version_checker('notebook', notebook_version)

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
    print('\tCustom kernel is correctly installed')
