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
    min=5,
    max=10.0,
    step=0.1,
    description='Text:',
    disabled=False
)
widgets.link((slider, 'value'), (bounded_float_text, 'value'))
widgets.link((slider, 'min'), (bounded_float_text, 'min'))
widgets.link((slider, 'max'), (bounded_float_text, 'max'))
widgets.VBox([slider, bounded_float_text])
