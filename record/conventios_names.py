# name variables according to PEP 8 conventions
my_variable = 10

another_variable = "Hello, World!"

def my_function(param_one, param_two):
    return param_one + param_two

class MyClass:
    def __init__(self, attribute_one, attribute_two):
        self.attribute_one = attribute_one
        self.attribute_two = attribute_two

    def display_attributes(self):
        print(f"Attribute One: {self.attribute_one}, Attribute Two: {self.attribute_two}")

# private variable example
_private_variable = 42

# constant variable example
CONSTANT_VALUE = 3.14

# function with descriptive name
def calculate_area(radius):
    return CONSTANT_VALUE * (radius ** 2)

# args and kwargs naming
def example_function(*args, **kwargs):
    for arg in args:
        print(f"Arg: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
if __name__ == "__main__":
    obj = MyClass("Value1", "Value2")
    obj.display_attributes()
    area = calculate_area(5)
    print(f"Area: {area}")
    example_function(1, 2, key1="value1", key2="value2")

# This code follows PEP 8 naming conventions for variables, functions, and classes.
