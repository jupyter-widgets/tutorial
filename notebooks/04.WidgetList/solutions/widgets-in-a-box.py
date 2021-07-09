import ipywidgets as widgets
a = widgets.Play(description='Value A', min=1, max=10, value=5)
b = widgets.IntText(description='Value B')

vbox = widgets.HBox(children=[a, b])
vbox
