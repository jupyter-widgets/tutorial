import ipywidgets as widgets
a = widgets.IntText(description='Value A')
b = widgets.IntSlider(description='Value B')

vbox = widgets.VBox(children=[a, b])
vbox
