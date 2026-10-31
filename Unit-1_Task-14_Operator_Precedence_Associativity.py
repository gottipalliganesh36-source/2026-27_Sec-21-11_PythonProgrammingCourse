# Python Program to Demonstrate Operator Precedence and Associativity

print("--- 1. Operator Precedence ---")
# Multiplication (*) has higher precedence than Addition (+)
result1 = 10 + 3 * 2
print(f"10 + 3 * 2 = {result1}")  
# Explanation: Evaluated as 10 + (3 * 2) = 16, not (10 + 3) * 2 = 26

# Using parentheses to override default precedence
result2 = (10 + 3) * 2
print(f"(10 + 3) * 2 = {result2}")  
# Explanation: Parentheses have the highest precedence, so (10 + 3) is evaluated first.


print("\n--- 2. Left-to-Right Associativity (Standard Arithmetic) ---")
# Addition, subtraction, multiplication, and division have left-to-right associativity
result3 = 20 - 5 - 3
print(f"20 - 5 - 3 = {result3}")  
# Explanation: Evaluated as (20 - 5) - 3 = 12, not 20 - (5 - 3) = 18


print("\n--- 3. Right-to-Left Associativity (Exponentiation) ---")
# The exponentiation operator (**) evaluates from right to left
result4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result4}")  
# Explanation: Evaluated as 2 ** (3 ** 2) -> 2 ** 9 = 512, 
# rather than (2 ** 3) ** 2 -> 8 ** 2 = 64


print("\n--- 4. Logical Operators Precedence ---")
# The 'and' operator has higher precedence than the 'or' operator
result5 = True or False and False
print(f"True or False and False = {result5}")  
# Explanation: Evaluated as True or (False and False) -> True or False = True