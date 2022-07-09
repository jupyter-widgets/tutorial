# The Jupyter Widget Ecosystem

## Tutorial, SciPy 2022

# https://github.com/jupyter-widgets/tutorial

# Installation

**NOTE**: These installation instructions install `ipywidgets` version 7.7. We anticipate that ipywidgets 8 will be released before the tutorial. If it, and all of the packages that we use that are dependent on `ipywidgets` have releases before the tutorial we will also provide ipywidgets 8 installation instructions.

Either way, we will include some of the new features of ipywidgets 8 in the tutorial.

### Installation instructions last updated 2022-07-09

#### Read this if you set up the tutorial environment before 2022-07-09

> We have added two packages to the list of requirements on 2022-07-09. To add those packages to the environment you have already
> created, either `conda install -c conda-forge mpl-interactions=0.22.0 orjson=3.7.7` or, if you use pip,
> `pip install mpl-interactions==0.22.0 orjson==3.7.7`. Do not panic if you cannot update your environment; these packages are used in
> only two or three cells.

We **strongly recommend** using the conda Python distribution. You can install either [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages) or the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but very, very large).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab. The instructions below assume you will be using JupyterLab.

*We will spend a few minutes at the beginning of the tutorial pointing out some of the features of JupyterLab from the perspective of people already familiar with Jupyter notebooks.*

There are also download instructions below for installation using pip, which should work with any Python distribution.

## Download this repository

You can do this with either `git clone https://github.com/jupyter-widgets/tutorial.git` at the command line or by downloading this repostiory as a [Zip file](https://github.com/jupyter-widgets/tutorial/archive/master.zip).

## conda installation instructions

The steps below will get you a working environment.

```bash
conda env create -f environment.yml

conda activate widgets-tutorial-2022

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix
```

### Windows users
The installation instructions were tested on an up-to-date version of Windows 10 Professional. If you encounter any issues on Windows please open an issue or contact us through slack.

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```bash
pip install -r requirements.txt

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix
```

## Check your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/jupyter-widgets/tutorial/master/install_check.py) and run it:

```bash
python install_check.py
```

## Using binder

Click the badge below to run the tutorial online:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-widgets/tutorial/main?urlpath=%2Flab%2Ftree%2Fnotebooks)

Many of the materials work without modification on mybinder.org without needing to install anything on your computer. However, this is *not* the recommended way to do the tutorial.


## Any ipywidgets or custom widgets library question?

Please join us on the Gitter channel: https://gitter.im/jupyter-widgets/Lobby

## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
