# The Jupyter Widget Ecosystem

## Tutorial, SciPy 2018

# https://github.com/jupyter-widgets/tutorial

# Installation

The code in the tutorial has been written using Python 3; though most of it may also work with Python 2.7.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab; a couple of esoteric corner cases may not work in JupyterLab. The instructions below explain the additional installation steps needed for JupyerLab.

*If you are familiar with Jupyter notebooks but have never used JupyterLab, you should either spend some time practicing with JupyterLab before this tutorial or use a plain notebook.*

There are download instructions below for installation using pip, which should work with any Python distribution.

## anaconda/miniconda installation instructions
### Last update: 29 Jun 2018, 1800CDT

The steps below will get you a working environment.

### Windows users planning to use JupyterLab

The instructions below need one of two modification to work on Windows if you are planning to do the tutorial in JupyterLab. Please see the section [Windows/nodejs workarounds](#windowsnodejs-workarounds) below the installation instructions.



### Installation instructions
```
conda create -n widgets-tutorial -c conda-forge python=3.6 pip notebook=5.5 numpy scikit-image scipy pandas=0.23 requests

conda activate widgets-tutorial

# Install widgets from conda-forge
conda install -c conda-forge ipywidgets=7.2 bqplot ipyvolume ipyleaflet pythreejs ipyevents

# Install one more package from a different channel
conda install -c wwt pywwt

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

# The remaining steps are necessary only if using JupyterLab:

# Install JupyterLab
conda install -c conda-forge jupyterlab nodejs=9.11

# Enable JupyterLab extensions, which may take several minutes
jupyter labextension install @jupyter-widgets/jupyterlab-manager bqplot ipyvolume jupyter-threejs jupyter-leaflet
```

## Windows/nodejs workarounds

Both of the fixes come from [this open conda issue](https://github.com/conda/conda/issues/7203).

#### Fix for Windows 10

Thanks to the tutorial participant who pointed this out on slack! The fix from the issue is:

> enable Win32 long paths. [On] windows10 pro, you can open Local Group Policy Editor, and open item Computer Configuration -> Administrative Templates -> System -> Filesystem -> Enable Win32 long paths and click it to make it enable.

#### Fix for Windows 7

This might also work for earlier versions of Windows, but has only been tested on Windows 7.

+  Edit the `.condarc` file in your home directory, adding this to it:

```
pkgs_dirs:
  - c:\conda-pkgs
```

+ Create a new environment this way: `conda create -p c:\widgets-tutorial`
+ Activate the environment: `conda activate c:\widgets-tutorial`
+ Replace the first line in the instructions below with:

`conda install -c conda-forge python=3.6 pip notebook=5.5 numpy scikit-image scipy pandas=0.23 requests`

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```
pip install notebook==5.5 ipywidgets numpy scipy scikit-image traitlets requests bqplot ipywidgets==7.2 ipyvolume matplotlib pandas==0.23 ipyleaflet pythreejs ipyevents pywwt

# If you are using JupyterLab, install with
pip install jupyterlab

# If you are using JupyerLab, also run the series of labextension install command in
# the conda instructions.
```

## Check your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/jupyter-widgets/tutorial/master/install_check.py) and run it:

```
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. *We anticipate making changes to the tutorial content through the end of June, 2018.*

## Using binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master)

Follow [mybinder.org](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master) to run the tutorial online.


## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
