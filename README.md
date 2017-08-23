# The Jupyter Widget Ecosystem

## Tutorial, JupyterCon 2017

# https://github.com/jupyter-widgets/tutorial

# Installation

The code in the tutorial has been written using Python 3; though most of it may also work with Python 2.7.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

There are download instructions below for installation using pip, which should work with any Python distribution.

## anaconda/miniconda installation instructions

The steps below will get you a working environment.

```
conda create -n widgets-tutorial notebook=5.0 numpy python=3.6 scikit-image scipy

# Mac/Linux:
source activate widgets-tutorial

# Windows:
activate widgets-tutorial

# Install widgets from conda-forge, which has ipywidgets 7.0
conda install -c conda-forge ipywidgets=7.0 traittypes

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix
```

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```
pip install ipywidgets
jupyter nbextension enable --sys-prefix --py widgetsnbextension
```

## Tutorial materials

To get the tutorial materials, clone this repository.

## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
