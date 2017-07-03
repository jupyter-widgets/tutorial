def calculate_password(change):
    import string
    import random
    length = change['new']
    # Generate a list of random letters of the correct length.
    password = [random.choice(string.ascii_letters) for _ in range(length)]
    password = ''.join(password)
    # Add a line below to set the value of the password_text
    password_text.value = password
