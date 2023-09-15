def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the function with keyword arguments
print_kwargs(name="John", age=30, city="New York")
