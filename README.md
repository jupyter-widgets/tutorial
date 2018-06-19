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

The steps below will get you a working environment.

```
conda create -n widgets-tutorial -c conda-forge python=3.6 notebook=5.5 numpy scikit-image scipy

conda activate widgets-tutorial

# Install widgets from conda-forge, which automatically enables notebook
# extensions, if necessary
conda install -c conda-forge traitlets requests bqplot ipywidgets=7.2 ipyvolume matplotlib pandas=0.23 ipyleaflet pythreejs ipyevents

# Install one more package from a different channel
conda install -c wwt pywwt

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

# The remaining steps are necessary only if using JupyterLab:

# Install JupyterLab
conda install -c conda-forge jupyterlab

# NOTE: Enabling all of the extension will take several minutes

# Enable ipywidgets in JupyterLab
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Enable bqplot in JupyterLab
jupyter labextension install bqplot

# Enable ipyvolume in JupyterLab
jupyter labextension install ipyvolume
jupyter labextension install jupyter-threejs  # also takes care of pythreejs

# Enable ipyleaflet in JupyterLab
jupyter labextension install jupyter-leaflet
```

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

To get the tutorial materials, clone this repository.

## Using binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master)

Follow [mybinder.org](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master) to run the tutorial online.


## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
