import ipywidgets as widgets
slider = widgets.FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Input:',
)
bounded_float_text = widgets.BoundedFloatText(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Text:',
    disabled=False
)
widgets.link((slider, 'value'), (bounded_float_text, 'value'))
widgets.VBox([slider, bounded_float_text])