from __future__ import print_function, division

from ipywidgets import Box, Layout, IntSlider, RadioButtons, Label, Checkbox, VBox, ToggleButtons, HBox
from traitlets import link

from model import PassGen, SPECIAL_GROUPS


class PassGenGUI(VBox):
    """
    Class to encapsulate the interface for a simple password generator.
    """
    def __init__(self):
        super(PassGenGUI, self).__init__(description='Password container')
        self.model = PassGen()
        self.layout.width = '100%'
        self.layout.align_items = 'flex-start'
        style = {'description_width': 'initial'}
        self._length = IntSlider(min=8, max=20,
                                 description='Password Length',
                                 style=style)
        
        # Link the password length to the model.
        link((self._length, 'value'), (self.model, 'password_length'))

        self._top_label = Label(value='Generated password:',
                                style=style)

        # Look at the source for _special_char_box to see the linking...
        self._special = self._special_char_box()

        self._numbers = Checkbox(description='Include 1 to 3 numbers in the password',
                                 style=style)

        # Link the checkbox value to the model...
        link((self._numbers, 'value'), (self.model, 'include_numbers'))
        self._password_text = Label(' ')
        
        # Indent the generated apssword a bit.
        self._password_text.layout.margin = '0 0 0 20px'
        
        # Link the password displayed to the appropriate property
        # of the model.
        link((self._password_text, 'value'), (self.model, 'password'))

        self.children = [self._top_label,
                         self._password_text,
                         self._length, self._special,
                         self._numbers]

    def _special_char_box(self):
        """
        The amount of space provided as a description in a ToggleButtons
        or a RadioButton is limited and the label is always to the left of
        the buttons. This makes a compound widget that has a 
        description over some buttons.

        Note that the linking to the model is handled here so that the calling
        code, __init__, does not need to know about the details of this widget.
        """

        explanation = Label('From 1 to 3 special characters from the group you select will be included.')
        special = ToggleButtons(options=SPECIAL_GROUPS)
        special.layout.margin = '0 0 0 20px'
        
        # This link establishes a connection to the model.
        link((special, 'value'),
             (self.model, 'special_character_groups'))

        container = VBox(description='Special character',
                         children=[explanation, special])
        container.layout.align_items = 'flex-start'
        return container