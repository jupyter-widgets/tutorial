import string
import inspect
from collections import defaultdict

import ipywidgets as widgets
from IPython.display import HTML


def extract_module_name(obj, full=False):
    """
    Get the name of a module for an object.
    """
    properties = inspect.getmembers(obj)
    for name, value in properties:
        if name == '__module__':
            if full:
                return value.split('.')[-1]
            else:
                return value
    else:
        raise ValueError('How odd...no moduel was found!')


def organized_widgets(organize_by='ui'):
    """
    Return a dictionary of all DOM widgets organized by either which module
    they are in or by the type of UI.

    Parameters
    ----------

    organize_by : str, optional
        Must be one of 'ui' or 'module'. Determines the keys in the returned
        dictionary.

    Returns
    -------

    dict
        Dictionary whose keys are the names of the widget groups and whose
        values are dictionaries. The dictionaries which are the values of
        ``groups`` have the name of the widget to be displayed as
        the key and the class of the widget as the value.
    """
    valid_organizations = ['ui', 'module']
    if organize_by not in valid_organizations:
        raise ValueError(f'Invalid value {organize_by} for organize_by. '
                          'Valid options are: {valid_organizations}')

    all_wids = inspect.getmembers(widgets)
 
    widget_dict = {name: wid for name, wid in all_wids
                   if not name.startswith('_') and
                      name[0] in string.ascii_uppercase and
                      issubclass(wid, widgets.DOMWidget) and
                      name != 'DOMWidget'
                  }

    if organize_by == 'ui':
        containers = ['Box', 'VBox', 'HBox', 'GridBox',
                      'Accordion', 'Tab', 'AppLayout', 'GridspecLayout',
                      'TwoByTwoLayout', 'Stacked']
        groups = dict(
            sliders={k: v for k, v in widget_dict.items() if 'Slider' in k},
            buttons={k: v for k, v in widget_dict.items() if 'Button' in k},
            containers={k: v for k, v in widget_dict.items() if k in containers},
            texts={k: v for k, v in widget_dict.items() if 'text' in k or 'Text' in k or 'HTML' in k or k in ['Label', 'Password']},
            progress={k: v for k, v in widget_dict.items() if 'Progress' in k},
            selects={k: v for k, v in widget_dict.items() if k in ['Dropdown', 'Select', 'SelectMultiple']},
            media={k: v for k, v in widget_dict.items() if k in ['Audio', 'Image', 'Play', 'Video']}
        )
        all_so_far = [name for k, v in groups.items() for name in v.keys()]
        groups['others'] = {k: v for k, v in widget_dict.items() if k not in all_so_far}
    elif organize_by == 'module':
        groups = defaultdict(dict)
        for k, v in widget_dict.items():
            module_name = extract_module_name(v)
            # Grab just the very last part of the module name for a nicer title
            module_name = module_name.split('_')[-1]
            groups[module_name][k] = v

    return groups


def fill_container(widget, name):
    """
    Many of the containers really need special set up; simply adding children does
    not do the trick. Hide those messy cases in here.
    """
    button_lay = widgets.Layout(width="auto", height="auto")
    if name == "gridspeclayout":
        for i in range(widget.n_rows):
            for j in range(widget.n_columns):
                widget[i, j] = widgets.Button(description='{}, {}'.format(i, j))
    elif name == "gridbox":
        widget.layout = widgets.Layout(grid_template_columns="repeat(3, 33%)")
        widget.children = [widgets.Button(description=str(i),
                                          layout=button_lay) for i in range(6)]
    elif name == "twobytwolayout":
        pass
        widget.top_left = widgets.Button(description="Top left")
        widget.top_right = widgets.Button(description="Top right")
        widget.bottom_left = widgets.Button(description="Bottom left")
        widget.bottom_right = widgets.Button(description="Bottom right")
    elif name == "applayout":
        # So replacing the layouts below with button_lay breaks the AppLayout
        # widget. No clue why.
        header        = widgets.Button(description="Header",
                                       layout=widgets.Layout(width="auto", height="auto"))
        left_sidebar  = widgets.Button(description="Left Sidebar",
                                       layout=widgets.Layout(width="auto", height="auto"))
        center        = widgets.Button(description="Center",
                                       layout=widgets.Layout(width="auto", height="auto"))
        right_sidebar = widgets.Button(description="Right Sidebar",
                                       layout=widgets.Layout(width="auto", height="auto"))
        footer        = widgets.Button(description="Footer",
                                       layout=widgets.Layout(width="auto", height="auto"))
        widget.header = header
        widget.left_sidebar = left_sidebar
        widget.center = center
        widget.right_sidebar = right_sidebar
        widget.footer = footer
    else:
        widget.children = [widgets.Button(description=str(i)) for i in range(3)]

    # Set tab or accordion names
    if name == "accordion" or name == "tab":
        titles = [f'{name} {idx}' for idx, _ in enumerate(widget.children)]
        try:
            # Retrieve the titles attribute to see if it exists
            widget.titles
        except AttributeError:
            for idx, title in enumerate(titles):
                widget.set_title(idx, title)
        else:
            widget.titles = titles

    # Start with all the accordions closed
    if name == "accordion":
        widget.selected_index = None


def list_overview_widget(groups,
                         help_url_base='',
                         columns=3,
                         min_width_single_widget=300):
    """
    Create an tab-based display of all of the widgets in ``groups``, with
    a separate tab for each key in groups and links to more detail for each
    widget. The first line of the docstring of each widget provides a
    short description of the widget.

    Parameters
    ----------

    groups : dict
        Dictionary whose keys are the names of the widget groups and whose
        values are dictionaries. The dictionaries which are the values of
        ``groups`` should have the name of the widget to be displayed as
        the key and the class of the widget as the value.
    help_url_base : str, optional
        URL to prepend to the help link for each widget.
    columns : int, optional
        Number of columns to use in displaying the widgets.
    min_width_single_widget : int, optional
        Minimum width, in pixels, of a widget displayed on a tab.

    Returns
    -------

    widgets.Tab
        A ``Tab`` widget with one tab for key of groups in which all of
        the widgets in that group are displayed.
    """

    tabs = widgets.Tab()

    if help_url_base is None:
        help_url_base = 'https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html'

    titles = []
    kids = []

    def box_maker(name, widget, group):
        layout = widgets.Layout(grid_template_columns="1fr",
                                border='2px solid gray')
        b = widgets.GridBox(layout=layout)
        module = extract_module_name(widget, full=True)

        if 'selection' in module:
            extra_args = dict(options=[1, 2, 3])
        elif 'progress' in widget.__name__.lower():
            extra_args = dict(value=50)
        elif 'gridspeclayout' in widget.__name__.lower():
            extra_args = dict(n_rows=3, n_columns=3)
        else:
            extra_args = {}

        wid = widget(description='A label!', **extra_args)

        try:
            short_description = wid.__doc__.split('\n')[0]
            if not short_description:
                short_description = wid.__doc__.split('\n')[1]
        except AttributeError:
            short_description = ''

        if group == 'containers':
            # These look better with things in them but need some custom code
            fill_container(wid, widget.__name__.lower())

        url = f'{help_url_base}#{name}'
        help_link = f'<h3><a href="{url}" rel="nofollow" target="_self" style="color:gray;">{name}</a></h3><p>{short_description}</p>'
        title = widgets.Output()
        title.append_display_data(HTML(help_link))
        title.layout.padding = '10px'
        b.layout.overflow_x = 'hidden'
        b.children = [title, wid]

        return b

    for group, group_widgets in groups.items():
        titles.append(group)
        col_spec = f"repeat({columns}, minmax({min_width_single_widget}px, 1fr)"
        layout = widgets.Layout(grid_template_columns=col_spec,
                                grid_gap='10px 10px')
        kid = widgets.GridBox(layout=layout)
        kid.children = [box_maker(k, v, group) for k, v in group_widgets.items()]
        kids.append(kid)

    tabs.children = kids

    try:
        # Try to access the titles attribute to see if it exists
        tabs.titles
    except AttributeError:
        # We must be using ipywidgets 7, so set_titles
        for i, title in enumerate(titles):
            nice = title.replace('_', ' ')
            tabs.set_title(i, nice.title())
    else:
        # We have ipywidgets 8
        tabs.titles = titles

    return tabs
