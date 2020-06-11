# The Jupyter Widget Ecosystem

## Tutorial, SciPy 2020

# https://github.com/jupyter-widgets/tutorial

# Installation

The code in the tutorial has been written using Python 3; many of the dependencies may not be available for Python 2.7.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab. The instructions below assume you will be using JupyterLab.

*We will spend a few minutes at the beginning of the tutorial pointing out some of the features of JupyterLab from the perspective of people already familiar with Jupyter notebooks.*

There are download instructions below for installation using pip, which should work with any Python distribution.

## anaconda/miniconda installation instructions
### Last update: 11 Jun 2020, 1000CDT

The steps below will get you a working environment.

### Windows users

The installation instructions below were tested on an up-to-date version of Windows 10 Professional. If you encounter any issues on Windows please open an issue or contact us through slack.

### Conda installation instructions

```
conda create -n widgets-tutorial -c conda-forge python=3.8 pip notebook numpy scikit-image scipy pandas requests ipywidgets bqplot ipyleaflet pythreejs ipycanvas ipyevents ipysheet ipytree ipympl pywwt sidecar voila=0.1 ipyvuetify voila-vuetify jupyterlab=2 nodejs=13 ipyvolume=0.6.0a6

conda activate widgets-tutorial

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

# Enable JupyterLab extensions, which may take several minutes
jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyter-widgets/jupyterlab-sidecar bqplot jupyter-threejs jupyter-leaflet ipysheet ipytree ipycanvas jupyter-matplotlib jupyter-vuetify ipyvolume
```

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```
pip install notebook numpy scipy scikit-image traitlets requests bqplot ipywidgets matplotlib pandas ipyleaflet pythreejs ipyevents ipysheet ipytree pywwt ipympl "voila>=0.1.2" "jupyterlab>=2" ipyvuetify voila-vuetify sidecar ipyvolume==0.6.0-a.6
```


#### Install nodejs

See [https://nodejs.org/en/download/](https://nodejs.org/en/download/) or [https://nodejs.org/en/download/package-manager/](https://nodejs.org/en/download/package-manager/) for download and installation instructions.

```
# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

# Enable JupyterLab extensions, which may take several minutes
jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyter-widgets/jupyterlab-sidecar bqplot jupyter-threejs jupyter-leaflet ipysheet ipytree ipycanvas jupyter-matplotlib jupyter-vuetify ipyvolume
```

## Check your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/jupyter-widgets/tutorial/master/install_check.py) and run it:

```
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. *We anticipate making changes to the tutorial content through the end of June, 2020.*

## Using binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master)

Many of the materials work without modification on mybinder.org without needing to install anything on your computer. However, this is *not* the recommended way to do the tutorial.

Go to [mybinder.org](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master) to run the tutorial online.


## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
