# As luas de Jupyter: widgets e outras ferramentas que o orbitam

Esse workshop é uma tradução do original: [The Jupyter Widget Ecosystem](https://github.com/jupyter-widgets/tutorial)

# Installation

### Installation instructions last updated 2021-06-07

The code in the tutorial has been written using Python 3; many of the dependencies may not be available for Python 2.7.

We **strongly recommend** using the conda Python distribution. You can install either [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages) or the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but very, very large).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab. The instructions below assume you will be using JupyterLab.

*We will spend a few minutes at the beginning of the tutorial pointing out some of the features of JupyterLab from the perspective of people already familiar with Jupyter notebooks.*

There are also download instructions below for installation using pip, which should work with any Python distribution.

## Download this repository

You can do this with either `git clone https://github.com/marimeireles/tutorial.git` at the command line or by downloading this repostiory as a [Zip file](https://github.com/jupyter-widgets/tutorial/archive/master.zip).

## conda/mamba installation instructions

The steps below will get you a  working environment.

```bash
conda env create -f environment.yml

conda activate luas-de-jupyter

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix
```

```bash
mamba env update --file environment.yml

conda activate luas-de-jupyter

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

## Tutorial materials

To get the tutorial materials, clone this repository. *We anticipate making changes to the tutorial content through the end of July 8, 2020.*

To update your copy of the tutorial materials, navigate in a terminal to folder these materials are in then run `git pull`. An alternative is to download the repository again as a zip file.

## Using binder

Click the badge below to run the tutorial online:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marimeireles/tutorial/master?urlpath=%2Flab%2Ftree%2Fnotebooks)

Many of the materials work without modification on mybinder.org without needing to install anything on your computer. However, this is *not* the recommended way to do the tutorial.


## Any ipywidgets or custom widgets library question?

Please join us on the Gitter channel: https://gitter.im/jupyter-widgets/Lobby

## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
