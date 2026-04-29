# **kwargs – variable keyword arguments
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", city="NY", course="Python")