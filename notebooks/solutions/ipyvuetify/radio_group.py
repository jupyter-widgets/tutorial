rg = v.RadioGroup(v_model=options[0],
                  children=[v.Radio(label=k, value=k) for k in options],
                  label="Pizza topping:")
rg