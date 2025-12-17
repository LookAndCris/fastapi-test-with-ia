# HOF

def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_operation(numbers, square)
print(squared_numbers)