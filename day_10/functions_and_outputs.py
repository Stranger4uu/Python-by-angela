def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name(f_name="Yash", l_name="saini")

length = len(formatted_name)
print(formatted_name)
print(length)