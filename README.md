# The Jupyter Widget Ecosystem

## Tutorial, SciPy 2019

# https://github.com/jupyter-widgets/tutorial

# Installation

The code in the tutorial has been written using Python 3; most of it may also work with Python 2.7.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab. The instructions below assume you will be using JupyterLab.

*We will spend a few minutes at the beginning of the tutorial pointing out some of the features of JupyterLab from the perspective of people already familiar with Jupyter notebooks.*

There are download instructions below for installation using pip, which should work with any Python distribution.

## anaconda/miniconda installation instructions
### Last update: 18 Jun 2019, 1500CDT

The steps below will get you a working environment.

### Windows users

The installation instructions below were tested on an up-to-date version of Windows 10 Professional. If you encounter any issues on Windows please open an issue or contact us through slack.
### Installation instructions

```
conda create -n widgets-tutorial -c conda-forge python=3.7 pip notebook numpy scikit-image scipy pandas requests ipywidgets bqplot ipyvolume ipyleaflet pythreejs ipyevents ipysheet ipytree ipympl pywwt voila=0.1 jupyterlab nodejs=11.14

conda activate widgets-tutorial

# Install ipyvuetify and voila-vuetify from pip (not on conda-forge yet)
pip install ipyvuetify voila-vuetify

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

# Enable JupyterLab extensions, which may take several minutes
jupyter labextension install @jupyter-widgets/jupyterlab-manager bqplot ipyvolume jupyter-threejs jupyter-leaflet ipysheet ipytree jupyter-matplotlib jupyter-vuetify
```

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```
pip install notebook==5.7 numpy scipy scikit-image traitlets requests bqplot ipywidgets ipyvolume matplotlib pandas ipyleaflet pythreejs ipyevents ipysheet ipytree pywwt ipympl "voila>=0.1.2" jupyterlab ipyvuetify voila-vuetify

# If you are using JupyerLab, also run the series of labextension install command in
# the conda instructions.
```

## Check your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/jupyter-widgets/tutorial/master/install_check.py) and run it:

```
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. *We anticipate making changes to the tutorial content through the end of June, 2019.*

## Using binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master)

Follow [mybinder.org](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/master) to run the tutorial online.


## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
