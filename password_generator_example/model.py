from __future__ import print_function, division

import string
import random

import traitlets

SPECIAL_GROUPS = [',./;[', '!@#~%', '^&*()']


class PassGen(traitlets.HasTraits):
    """
    Class to represent state of password generator and handle generation
    of password.
    """
    password_length = traitlets.Integer()
    include_numbers = traitlets.Bool()
    special_character_groups = traitlets.Enum(SPECIAL_GROUPS,
                                              default_value=SPECIAL_GROUPS[0])
    password = traitlets.Unicode("password")

    def __init__(self):
        super(PassGen, self).__init__(description='Password model')
        pass

    # The observe decorator is used to indicate that the function being
    # decorated should be called if any of the traits listed as arguments
    # change. The decorated function must have an argument named change;
    # in this example the change variable isn't used because we want to update
    # the generated password no matter what the change was.
    @traitlets.observe('password_length',
                       'include_numbers',
                       'special_character_groups')
    def generate_password(self, change):
        """
        Generate a password of the desired length including the user's chosen
        set of special characters and, if desired, including some numerals.
        """

        # Generate an initial password composed only of letters.
        new_pass = []
        for _ in range(self.password_length):
            new_pass.append(random.choice(string.ascii_letters))

        # Generate a list of indices for choosing which characters in the
        # initial password to replace, then shuffle it. We'll pop
        # elements off the list as we need them.
        order_for_replacements = list(range(self.password_length))
        random.shuffle(order_for_replacements)

        # Replace some of the letters with special characters
        n_special = random.randint(1, 3)
        for _ in range(n_special):
            loc = order_for_replacements.pop(0)
            new_pass[loc] = random.choice(self.special_character_groups)

        if self.include_numbers:
            # Number of digits to include.
            n_digits = random.randint(1, 3)
            for _ in range(n_digits):
                loc = order_for_replacements.pop(0)
                new_pass[loc] = random.choice(string.digits)

        self.password = ''.join(new_pass)
