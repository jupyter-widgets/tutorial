# Thanks to [Doug Redden (@DougRzz)](https://github.com/DougRzz) for contributing the code this file was based on.

__all__ = ['layout']

import numpy as np
import ipywidgets as widgets
from traitlets import TraitError

item_layout = widgets.Layout(height='80px', min_width='30px', min_height='50px', width ='60px',flex_wrap='wrap')
button_styles = ['primary',
'success',
'info',
'warning',
'danger']
item_layout_options = dict(min_width='30px', min_height='20px', width ='60px',flex_wrap='wrap')

def make_items(n):
    items = [widgets.Button(layout=widgets.Layout(**item_layout_options), description=str(i), button_style=button_styles[i % 5]) for i in range(n)]
    # Randomize heights so it is a little clearer what some of the layout
    # options do.
    for item in items:
        item.layout.min_height = '20px'
        item.layout.height = '{}px'.format(np.random.choice([20, 25, 50, 67, 80]))
    return items

initial_number_of_buttons = 18
items = make_items(initial_number_of_buttons)

# ### Create box to hold the layout demo widgets
#
# The widget displayed below will be embedded in a larger widget later in the notebook. That larger widget lets you interactively change the layout of this widget.

# In[ ]:

default_options = dict(
    border='3px solid gray',
    width='700px',
    min_width='50px',
    max_width='1000px',
    min_height='50px',
    max_height='1000px',
    height='300px',
    flex_flow='row nowrap',
    display='flex',
    justify_content='flex-start',
    align_items='stretch',
    align_content='stretch'
)

box_layout = widgets.Layout(**default_options)


def _set_overflow_from_x_y(layout, ox, oy):
    """
    Hide the ugly logic for packing/unpacking overflow
    from the rest of the code.
    """
    layout._overflow = '{} {}'.format(ox, oy)
    try:
        layout.overflow = layout._overflow
    except TraitError:
        # Oh well, not using 7.5 yet I guess...
        layout.overflow_x = ox
        layout.overflow_y = oy

_set_overflow_from_x_y(box_layout, 'scroll', 'scroll')


def _get_overflow_x_y():
    try:
        x, y = widgetGroup.layout.overflow.split(' ')
    except AttributeError:
        # We invented a hidden overflow property above in case
        # the 7.5 style overflow doesn't work...
        x = widgetGroup.layout.overflow_x
        y = widgetGroup.layout.overflow_y

    return x, y


widgetGroup = widgets.Box(children=items, layout=box_layout)

widgetGroupAndTitle = widgets.VBox([widgets.Label('Widget area:'), widgetGroup],
                                   layout=widgets.Layout(height='500px', width ='700px'))

widgetGroupAndTitle


# ## Construct widget with controls for changing layout

# ### Create a text area widget where the Python code to reproduce the CSS programmatically.

# In[ ]:


pythonCode = widgets.Textarea(
    value='',
    placeholder='Python code is exported to this panel....',
    description='',
    disabled=False
)

pythonCode.layout.width = '80%'
pythonCode.layout.height = '80px'


# ### Create drop downs for choices of `overflow` in `x` and `y`

# In[ ]:


# Set a uniform description width to make alignment easier
style = {'description_width': '100px'}

# Define a layout for groups of properties in a shortcut
shortcut_group_layout = widgets.Layout(border='2px dotted gray',
                                       width='fit-content')

# Define one of two lists that will hold controls for changing the layout
vboxList = []


overflow_shortcut = widgets.Text(description='overflow',
                                 disabled=True)
overflow_shortcut.value = '{} {}'.format(*_get_overflow_x_y())

overflow_kids = []

# Widget to present overflow style options for x
overflow_x = widgets.Dropdown(
    options=['scroll','hidden','auto','visible','initial','inherit'] ,
    value = widgetGroup.layout.overflow_x,
    description='overflow_x:',
    disabled=False,
    style=style,
)

# Add the
#vboxList.append(overflow_x)

# Set up observer to watch for changes in selected overflow style and apply
# selected style to widgetGroup.
def on_overflow_xchange(change):
    if change['type'] == 'change' and change['name'] == 'value':
        old_x, old_y = _get_overflow_x_y()
        _set_overflow_from_x_y(widgetGroup.layout, change.new, old_y)
        overflow_shortcut.value = '{} {}'.format(*_get_overflow_x_y())

        # Note how easy it is to get the Python code to generate the layout!
        pythonCode.value = str(widgetGroup.layout)

overflow_x.observe(on_overflow_xchange)


# Widget to present overflow style options for y

overflow_y = widgets.Dropdown(
    options=['scroll','hidden','auto','visible','initial','inherit'] ,
    value='scroll',
    description='overflow_y:',
    disabled=False,
    style=style,
)


def on_overflow_y_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        old_x, old_y = _get_overflow_x_y()
        _set_overflow_from_x_y(widgetGroup.layout, old_x, change.new)
        overflow_shortcut.value = '{} {}'.format(*_get_overflow_x_y())
        pythonCode.value = str(widgetGroup.layout)


overflow_y.observe(on_overflow_y_change)

overflow_box = widgets.VBox(children=[overflow_shortcut,
                                      overflow_x,
                                      overflow_y],
                            layout=shortcut_group_layout)


def reset_overflow():
    """
    Set overflow_x/y from overflow.
    """
    overflow_shortcut.value = '{} {}'.format(*_get_overflow_x_y())
    overflow_x.value, overflow_y.value = _get_overflow_x_y()


vboxList.append(overflow_box)

# ### Add some choices for the border around our layout demo

# In[ ]:

border_box = widgets.VBox(layout=shortcut_group_layout)

border_shortcut = widgets.Text(description="border",
                               disabled=True,
                               value=widgetGroup.layout.border)


def _get_border_pieces():
    return widgetGroup.layout.border.split(' ')


bwid, bstyle, bcolor = _get_border_pieces()

border_width = widgets.Text(description="width:",
                            value=bwid,
                            style=style)


def _update_border():
    widgetGroup.layout.border = ' '.join([border_width.value,
                                          border_style.value,
                                          border_color.value])
    border_shortcut.value = widgetGroup.layout.border


def on_border_width_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        _update_border()
        pythonCode.value = str(widgetGroup.layout)

border_width.observe(on_border_width_change)

border_style = widgets.Dropdown(
    options=['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'],
    value=bstyle,
    description='style:',
    style=style
)


def on_border_style_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        _update_border()
        pythonCode.value = str(widgetGroup.layout)


border_style.observe(on_border_style_change)

border_color = widgets.Text(description="color:",
                            value=bcolor,
                            style=style)


def on_border_color_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        _update_border()
        pythonCode.value = str(widgetGroup.layout)


border_color.observe(on_border_color_change)


# border = widgets.Dropdown(
#     options=['3px solid gray', '1px dashed black','2px solid black','3px solid blue', ],
#     value = widgetGroup.layout.border,
#     description='border:',
#     disabled=False,
#     style=style,
# )

border_box.children = [
    border_shortcut,
    border_width,
    border_style,
    border_color
]
vboxList.append(border_box)


def reset_border():
    border_shortcut.value = widgetGroup.layout.border
    border_width.value, border_style.value, border_color.value = \
        _get_border_pieces()


# def on_border_change(change):
#     if change['type'] == 'change' and change['name'] == 'value':
#         widgetGroup.layout.border = change.new
#         pythonCode.value = str(widgetGroup.layout)

# border.observe(on_border_change)


# ## Add dropdowns for several CSS layout options

# In[ ]:

# display options

display = widgets.Dropdown(
    options=['flex', 'inline-flex'],
    value='flex',
    description='display:',
    disabled=False,
    style=style,
)
# vboxList.append(display)
def on_display_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.display = change.new
        pythonCode.value = str(widgetGroup.layout)

display.observe(on_display_change)

flex_flow = widgets.VBox(layout=shortcut_group_layout)
flex_flow_list = []

flex_flow_shortcut = widgets.Text(description='flex_flow',
                                  value=widgetGroup.layout.flex_flow,
                                  disabled=True)
flex_flow_list.append(flex_flow_shortcut)
# flex-flow options

flex_flow_dir = widgets.Dropdown(
    options=[
        'column-reverse',
        'column',
        'row',
        'row-reverse',
    ],
    value='row',
    description='direction:',
    disabled=False,
    style=style,
)
flex_flow_list.append(flex_flow_dir)
def on_flex_flow_dir_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        flex_flow = widgetGroup.layout.flex_flow
        direction, wrap = flex_flow.split(' ')
        direction = change.new
        widgetGroup.layout.flex_flow = direction + ' ' + wrap
        flex_flow_shortcut.value = widgetGroup.layout.flex_flow
        pythonCode.value = str(widgetGroup.layout)

flex_flow_dir.observe(on_flex_flow_dir_change)


# flex-wrap options

flex_wrap = widgets.Dropdown(
    options=[
        'nowrap',
        'wrap',
        'wrap-reverse',
    ],
    value='nowrap',
    description='wrap:',
    disabled=False,
    style=style,
)
flex_flow_list.append(flex_wrap)
def on_flex_wrap_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        flex_flow = widgetGroup.layout.flex_flow
        if flex_flow is not None:
            flex_flow = flex_flow.split(' ')
        else:
            flex_flow = ['']
        widgetGroup.layout.flex_flow = flex_flow[0] + ' ' + change.new
        flex_flow_shortcut.value = widgetGroup.layout.flex_flow
        pythonCode.value = str(widgetGroup.layout)

flex_wrap.observe(on_flex_wrap_change)

flex_flow.children = flex_flow_list

vboxList.append(flex_flow)
# justify-content options

main_axis_box = widgets.VBox(layout=shortcut_group_layout)

main_axis_label = widgets.Label(value="Main axis")

justify_content = widgets.Dropdown(
    options=[
        'flex-start',
        'flex-end',
        'center',
        'space-between',
        'space-around',
    ],
    value=widgetGroup.layout.justify_content,
    description='justify_content:',
    disabled=False,
    style=style,
)

def on_justify_content_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.justify_content = change.new
        pythonCode.value = str(widgetGroup.layout)

justify_content.observe(on_justify_content_change)

main_axis_box.children = [
    main_axis_label,
    justify_content
]

vboxList.append(main_axis_box)


cross_axis_box = widgets.VBox(layout=shortcut_group_layout)

cross_axis_label = widgets.Label(value='Cross axis')
# align-items options

align_items = widgets.Dropdown(
    options=[
        'flex-start',
        'flex-end',
        'center',
        'baseline',
        'stretch',
    ],
    value=widgetGroup.layout.align_items,
    description='align_items:',
    disabled=False,
    style=style,
)

def on_align_items_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.align_items = change.new
        pythonCode.value = str(widgetGroup.layout)

align_items.observe(on_align_items_change)


# align-content options

align_content = widgets.Dropdown(
    options=[
        'flex-start',
        'flex-end',
        'center',
        'space-between',
        'space-around',
        'space-evenly',
        'stretch',
        'inherit',
        'initial',
        'unset'],
    value=widgetGroup.layout.align_content,
    description='align_content:',
    disabled=False,
    style=style,
)

def on_align_content_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.align_content = change.new
        pythonCode.value = str(widgetGroup.layout)

align_content.observe(on_align_content_change)

cross_axis_box.children = [
    cross_axis_label,
    align_items,
    align_content
]

vboxList.append(cross_axis_box)

# ### Set up `VBox` for holding these controls

# In[ ]:


# vbox_style_options  = widgets.VBox(vboxList)
grid_layout = widgets.Layout(grid_template_rows="repeat(2, auto)",
                             grid_auto_flow="column dense",
                             grid_auto_colums="repeat(2, 1fr)",
                             grid_gap="10px",
                             width="100%")
vbox_style_options = widgets.GridBox(vboxList,
                                     layout=grid_layout)

# ## Set up controls for changing sizes of layout demo

# In[ ]:


# These controls will be grouped together in one VBox. Items added to the list
# below will be placed in that VBox

vboxwidgetSizeList =[]


sizeButtonWidth = '40px'
buttonLayout = widgets.Layout(width=sizeButtonWidth)

# Button/slider combination for adjusting width
width_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)
width_px_percent.style.button_width = sizeButtonWidth

width = widgets.IntSlider(
    value = int(widgetGroup.layout.width.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='width:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
def on_width_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.width = str(change.new) + width_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

width.observe(on_width_change)



vboxwidgetSizeList.append(widgets.HBox([width, width_px_percent]))

def on_width_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.width = str(width.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

width_px_percent.observe(on_width_px_percent_change)


# In[ ]:


# Same as above, but for height

height = widgets.IntSlider(
    value = int(widgetGroup.layout.height.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='height:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
def on_height_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.height = str(change.new) + height_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

height.observe(on_height_change)

height_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)

height_px_percent.style.button_width = sizeButtonWidth   # ipywidgets 7.0 and above

vboxwidgetSizeList.append(widgets.HBox([height, height_px_percent]))

def on_height_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.height = str(height.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

height_px_percent.observe(on_height_px_percent_change)


# In[ ]:


# Slider/buttons for min-width

min_width = widgets.IntSlider(
    value=int(widgetGroup.layout.min_width.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='min_width:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

def on_min_width_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.min_width = str(change.new) + min_width_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

min_width.observe(on_min_width_change)


min_width_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)

min_width_px_percent.style.button_width = sizeButtonWidth   # ipywidgets 7.0 and above

vboxwidgetSizeList.append(widgets.HBox([min_width, min_width_px_percent]))

def on_min_width_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.min_width = str(min_width.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

min_width_px_percent.observe(on_min_width_px_percent_change)


# In[ ]:


# Now set up max-width controls

max_width = widgets.IntSlider(
    value=int(widgetGroup.layout.max_width.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='max_width:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

def on_max_width_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.max_width = str(change.new) + max_width_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

max_width.observe(on_max_width_change)


max_width_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)

max_width_px_percent.style.button_width = sizeButtonWidth   # ipywidgets 7.0 and above

vboxwidgetSizeList.append(widgets.HBox([max_width, max_width_px_percent]))

def on_max_width_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.max_width = str(max_width.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

max_width_px_percent.observe(on_max_width_px_percent_change)


# In[ ]:


# max-height controls
max_height = widgets.IntSlider(
    value=int(widgetGroup.layout.max_height.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='max_height:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

def on_max_height_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.max_height = str(change.new) + max_height_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

max_height.observe(on_max_height_change)

max_height_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)

max_height_px_percent.style.button_width = sizeButtonWidth   # ipywidgets 7.0 and above

vboxwidgetSizeList.append(widgets.HBox([max_height, max_height_px_percent]))

def on_max_height_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.max_height = str(max_height.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

max_height_px_percent.observe(on_max_height_px_percent_change)


# In[ ]:


# min-height controls
min_height = widgets.IntSlider(
    value=int(widgetGroup.layout.min_height.replace('%','').replace('px','')),
    min=0,
    max=1000,
    step=1,
    description='min_height:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

def on_min_height_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.min_height = str(change.new) + min_height_px_percent.value
        pythonCode.value = str(widgetGroup.layout)

min_height.observe(on_min_height_change)

min_height_px_percent = widgets.ToggleButtons(
    options=['px', '%',],
    description='',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Pixels', 'Percent of page',],
)

min_height_px_percent.style.button_width = sizeButtonWidth

vboxwidgetSizeList.append(widgets.HBox([min_height, min_height_px_percent]))

def on_min_height_px_percent_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.min_height = str(min_height.value) + change.new
        pythonCode.value = str(widgetGroup.layout)

min_height_px_percent.observe(on_min_height_px_percent_change)


# ### Create `VBox` to hold size controls

# In[ ]:


widgetSizeVbox  = widgets.VBox(vboxwidgetSizeList)


# ### Collate all the widgets and display

# In[ ]:

number_of_buttons = widgets.BoundedIntText(min=1, max=100, step=1,
                                           value=initial_number_of_buttons,
                                           description='Number of buttons',
                                           style={'description_width': 'initial'})


def on_number_of_buttons_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        items = make_items(change.new)
        widgetGroup.children = items

number_of_buttons.observe(on_number_of_buttons_change)


tabs = widgets.Tab()
tabs.children = [vbox_style_options, widgetSizeVbox, pythonCode]
tabs.set_title(0, 'Layout options')
tabs.set_title(1, 'Size options')
tabs.set_title(2, 'Python code')

reset_button = widgets.Button(description='Reset')


def on_reset_button(_):
    widgetGroup.layout = widgets.Layout(**default_options)
    pythonCode.value = str(widgetGroup.layout)
    _set_overflow_from_x_y(widgetGroup.layout, 'scroll', 'scroll')
    reset_overflow()
    reset_border()
    justify_content.value = widgetGroup.layout.justify_content
    align_content.value = widgetGroup.layout.align_content
    align_items.value = widgetGroup.layout.align_items
    number_of_buttons.value = initial_number_of_buttons


reset_button.on_click(on_reset_button)

hbox  = widgets.HBox([number_of_buttons, reset_button])
layout = widgets.VBox([hbox, tabs, widgetGroupAndTitle, ])
pythonCode.value = str(widgetGroup.layout)
layout

