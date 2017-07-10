# The Jupyter Widget Ecosystem

## Tutorial, SciPy 2017

# Installation -- last updated 6 July 2017, 21:28 CDT

The code in the tutorial has been written using Python 3; though it should also work with Python 2.7, it has not been tested extensively against that version.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

There are download instructions below for installation using pip, which should work with any Python distribution, and the script for checking your installation should run on any python.

## anaconda/miniconda installation instructions

The steps below will get you a working environment. Note that *the numpy version is important* as of the last update to the instructions because the numpy 1.13 package on anaconda appears to be broken.

```
conda create -n widgets-2017 notebook numpy=1.12 python=3.6 scikit-image scipy

# Mac/Linux:
source activate widgets-2017

# Windows:
activate widgets-2017

# Create a kernel for this environment
ipython kernel install --name widgets-2017 --display-name widgets-2017 --sys-prefix

conda install -c conda-forge traittypes

conda install -c astropy ccdproc ginga

pip install --pre ipywidgets bqplot ipyleaflet ipyvolume
jupyter nbextension enable --py widgetsnbextension
jupyter nbextension enable --py bqplot
jupyter nbextension enable --py ipyleaflet
jupyter nbextension enable --py ipyvolume
conda install -c conda-forge --force pythreejs
```

## pip installation instructions

If you are using the anaconda python distribution, please use the conda installation instructions above.

```
pip install --pre ipywidgets
jupyter nbextension enable --py widgetsnbextension

pip install astropy ccdproc ginga

pip install bqplot ipyleaflet ipyvolume pythreejs

jupyter nbextension enable --py bqplot
jupyter nbextension enable --py ipyvolume
jupyter nbextension enable --py pythreejs
jupyter nbextension enable --py ipyleaflet
```

## Testing your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/mwcraig/scipy2017-jupyter-widgets-tutorial/master/install_check.py) and run it:

```
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. **Please plan to update the materials shortly before the tutorial.**

## Running into trouble?

Please let us know! Either:

+ Open an issue on this repository.
+ Let us know on the slack channel for the tutorial.
+ Contact [mwcraig](https://github.com/mwcraig).


