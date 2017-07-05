**More detailed setup instructions**

With pip:

pip install ipywidgets bqplot ipyvolume pythreejs ipyleaflet\
jupyter nbextension enable --py widgetsnbextension

jupyter nbextension enable --py bqplot

jupyter nbextension enable --py ipyvolume

jupyter nbextension enable --py pythreejs

jupyter nbextension enable --py ipyleaflet

Note: see
[*http://ipywidgets.readthedocs.io/en/latest/user\_install.html*](http://ipywidgets.readthedocs.io/en/latest/user_install.html)
for instructions for installing in a virtualenv. If Python is installed
system-wide you may need to use the --user option.

With conda:

conda install -c conda-forge ipywidgets bqplot ipyvolume pythreejs
ipyleaflet

# Outline

1.  Widget definition/overview - ipywidgets objects have three pieces
    a.  JavaScript, which represents and renders the element in the browser
    b.  Python objects with an API for controlling display and content and for retrieving the properties of the widget.
    c.  Communication model, which handles the interaction between JavaScript and Python.
1.  Widget building blocks
    i.  Review list of widgets
        1.  Execute Widget List notebook from ipywidgets repo

        2.  Modify properties of a couple of the widgets

        3.  Get/set widget values from Python in code cell

    ii. Container widgets

        1.  ipywidgets 6 model for this: Layout widget in which
            > components can be vertical or horizontal

        2.  Add widgets to container by adding them as children of
            > the Layout widget

    iii. EXERCISE 1: three widgets (participant chooses which three)
        > laid out horizontally.

    iv. EXERCISE 2: two different widgets, laid out horizontally,
        > one Label plus one other, with Label replacing default
        > description area of second widget.

    v.  EXERCISE 3: Combine the widgets from the previous two
        > exercises into a single widget with the EX1 widget
        > vertically above the EX2 widget.

    vi. EXERCISE 4: Combine previous three widgets in a Tab
        > or Accordion.

e.  HTML widget -- embed any almost any web content in a widget

f.  Widget styling

    i.  Python interface to CSS properties via layout

    ii. Styling flex boxes.

g.  Embedding widgets in contexts other than the notebook

    i.  Sphinx documentation

    ii. Static web pages

    iii. nbviewer

h.  Basic GUIs with @interact

2.  Break: 5 minutes

3.  Widget libraries

    a.  2-D charting with bqplot

    b.  3D visualization

        i.  ipyvolume

        ii. Pythreejs

    c.  Mapping with ipyleaflet

    d.  Connecting widgets with events

4.  Break: 5 minutes

5.  Writing your own widgets

    a.  Widget events

        i.  Execute Widget Events notebook from ipywidgets repo.

        ii. Discussion/demo: link vs dlink vs jslink vs jsdlink

        iii. EXERCISE: Using events to make one widget change another

            1.  Make a container widget with a text box, a slider and a
                > Valid widget.

            2.  Link the value in text box to the description of the
                > slider

            3.  Set the Valid widget to True if the slider is in the
                > middle 50% of its range.

    b.  Building widgets -- two reasonable patterns:

        i.  Make a container widget, add pieces as children.

            1.  Good for prototyping.

            2.  Can be reused (write a function that returns one of
                > your containers).

        ii. Define a class that subclasses a container like Box

            1.  Good for reuse; your widget class is like any other
                > widget class as far as ipywidgets is concerned.

            2.  Pieces (i.e. the basic widgets) are still children.

        iii. Examples from reducer (or other sources)

    c.  EXERCISE: Construct a widget for generating passwords

        i.  Model class: Define inputs as traitlets, method for
            > generating password

        ii. View class: One widget for each input, composed in a Box

        iii. Controller: link traitlets in model and view, decorate
            > password method with observe.

6.  BREAK: 5 minutes

7.  Making your own controls with Python and JavaScript

    a.  Overview of front-end infrastructure

    b.  Start new project with widget-cookiecutter

    c.  EXERCISE: Develop custom control


