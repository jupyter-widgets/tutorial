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
    'ipysheet',
    'ipytree',
    'pywwt'
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

version_check_packages = {'ipywidgets': '7.4',
                          'notebook': '5.7',
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
    print('\tVoila is not installed! Please install it by running:')
    print('        conda install -c conda-forge voila')
    print('        pip install voila')

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
