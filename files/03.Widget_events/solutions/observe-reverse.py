text = widgets.Textarea()
output = widgets.Output()

@output.capture()
def reverse(change):
    print(change['new'][::-1])

text.observe(reverse, names='value')

display(text, output)
