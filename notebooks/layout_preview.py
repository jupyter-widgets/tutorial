

__all__ = ['layout']

import ipywidgets as widgets


item_layout = widgets.Layout(height='80px', min_width='30px', min_height='50px', width ='60px',flex_wrap='wrap')
button_styles = ['primary',
'success',
'info',
'warning',
'danger']

items = [widgets.Button(layout=item_layout, description=str(i), button_style=button_styles[i]) for i in range(5)]


# ### Create box to hold the layout demo widgets
#
# The widget deisplayed below will be embedded in a larger widget later in the notebook. That larger widget lets you interactively change the layout of this widget.

# In[ ]:


box_layout = widgets.Layout(overflow_x='scroll',
                    border='3px solid black',
                    width='700px',
                    min_width='50px',
                    max_width='1000px',
                    min_height='50px',
                    max_height='1000px',
                    height='300px',
                    flex_direction='row',
                    display='flex')

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

# Define one of two lists that will hold controls for changing the layout
vboxList = []

# Widget to present overflow style options for x
overflow_x = widgets.Dropdown(
    options=['scroll','hidden','auto','visible','initial','inherit'] ,
    value = widgetGroup.layout.overflow_x,
    description='overflow_x:',
    disabled=False,
    style=style,
)

# Add the
vboxList.append(overflow_x)

# Set up observer to watch for changes in selected overflow style and apply
# selected style to widgetGroup.
def on_overflow_xchange(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.overflow_x = change.new

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
vboxList.append(overflow_y)


def on_overflow_y_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.overflow_y = change.new
        pythonCode.value = str(widgetGroup.layout)

overflow_y.observe(on_overflow_y_change)


# ### Add some choices for the border around our layout demo

# In[ ]:


border = widgets.Dropdown(
    options=['3px solid black', '1px dashed black','2px solid black','3px solid blue', ],
    value = widgetGroup.layout.border,
    description='border:',
    disabled=False,
    style=style,
)

vboxList.append(border)

def on_border_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.border = change.new
        pythonCode.value = str(widgetGroup.layout)

border.observe(on_border_change)


# ## Add dropdowns for several CSS layout options

# In[ ]:


# flex-flow opetions

flex_flow = widgets.Dropdown(
    options=[
        'column-reverse',
        'column',
        'row',
        'row-reverse',
    ],
    value='row',
    description='flex-flow:',
    disabled=False,
    style=style,
)
vboxList.append(flex_flow)
def on_flex_flow_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.flex_flow = change.new
        pythonCode.value = str(widgetGroup.layout)

flex_flow.observe(on_flex_flow_change)

# flex-direction options
flex_direction = widgets.Dropdown(
    options=[
        'column-reverse',
        'column',
        'row',
        'row-reverse',
    ],
    value='row',
    description='flex-direction:',
    disabled=False,
    style=style,
)
vboxList.append(flex_direction)
def on_flex_direction_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.flex_direction = change.new
        pythonCode.value = str(widgetGroup.layout)

flex_direction.observe(on_flex_direction_change)

# display options

display = widgets.Dropdown(
    options=['flex', 'inline-flex'],
    value='flex',
    description='display:',
    disabled=False,
    style=style,
)
vboxList.append(display)
def on_display_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.display = change.new
        pythonCode.value = str(widgetGroup.layout)

display.observe(on_display_change)

# flex-wrap options

flex_wrap = widgets.Dropdown(
    options=[
        'nowrap',
        'wrap',
        'wrap-reverse',
    ],
    value='nowrap',
    description='flex-wrap:',
    disabled=False,
    style=style,
)
vboxList.append(flex_wrap)
def on_flex_wrap_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.flex_wrap = change.new
        pythonCode.value = str(widgetGroup.layout)

flex_wrap.observe(on_flex_wrap_change)

# justify-content options

justify_content = widgets.Dropdown(
    options=[
        'flex-start',
        'flex-end',
        'center',
        'space-between',
        'space-around',
    ],
    value='flex-start',
    description='justify_content:',
    disabled=False,
    style=style,
)

vboxList.append(justify_content)
def on_justify_content_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.justify_content = change.new
        pythonCode.value = str(widgetGroup.layout)

justify_content.observe(on_justify_content_change)

# align-items options

align_items = widgets.Dropdown(
    options=[
        'flex-start',
        'flex-end',
        'center',
        'baseline',
        'stretch',
    ],
    value='stretch',
    description='align_items:',
    disabled=False,
    style=style,
)
vboxList.append(align_items)
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
    value='stretch',
    description='align_content:',
    disabled=False,
    style=style,
)
vboxList.append(align_content)
def on_align_content_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        widgetGroup.layout.align_content = change.new
        pythonCode.value = str(widgetGroup.layout)

align_content.observe(on_align_content_change)


# ### Set up `VBox` for holding these controls

# In[ ]:


vbox_style_options  = widgets.VBox(vboxList)


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


hbox  = widgets.HBox([vbox_style_options, widgetSizeVbox, ])
layout  = widgets.VBox([pythonCode, hbox, widgetGroupAndTitle, ])

layout

