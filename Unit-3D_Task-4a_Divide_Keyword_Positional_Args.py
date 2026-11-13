# Function defined using two parameters
def divide(a, b):
    return a / b

result = divide(b=10, a=20)  # Keyword arguments
print(result)  # Output: 2.0

result = divide(10, 20)  # Positional arguments
print(result)  # Output: 0.5
# Example: function defined using two parameters
def divide(a , b ):  # a, b are 2 parameters
    return a / b

result = divide( b=10, a=20)  # with keyword arguments
print(result)  # Output: 2.0

result = divide(10 , 20)  # positional arguments
print(result)  # Output: 0.5