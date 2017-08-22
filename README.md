# The Jupyter Widget Ecosystem

## Tutorial, JupyterCon 2017

# Installation -- last updated 22 Aug, 4PM EDT

The code in the tutorial has been written using Python 3; though it may also work with Python 2.7, it has not been tested extensively against that version.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

There are download instructions below for installation using pip, which should work with any Python distribution, and the script for checking your installation should run on any Python.

## anaconda/miniconda installation instructions

The steps below will get you a working environment.

```
conda create -n widgets-tutorial notebook numpy python=3.6 scikit-image scipy

# Mac/Linux:
source activate widgets-tutorial

# Windows:
activate widgets-tutorial

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix

conda install -c conda-forge traittypes ipywidgets

pip install --pre bqplot ipyleaflet ipyvolume pythreejs
jupyter nbextension enable --sys-prefix --py bqplot
jupyter nbextension enable --sys-prefix --py ipyleaflet
jupyter nbextension enable --sys-prefix --py ipyvolume
jupyter nbextension enable --sys-prefix --py pythreejs
```

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```
pip install ipywidgets
pip install --pre bqplot ipyleaflet ipyvolume pythreejs
jupyter nbextension enable --sys-prefix --py widgetsnbextension
jupyter nbextension enable --sys-prefix --py bqplot
jupyter nbextension enable --sys-prefix --py ipyleaflet
jupyter nbextension enable --sys-prefix --py ipyvolume
jupyter nbextension enable --sys-prefix --py pythreejs
```

## Testing your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/mwcraig/scipy2017-jupyter-widgets-tutorial/master/install_check.py) and run it:

```
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. **Please plan to update the materials shortly before the tutorial.**

## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
