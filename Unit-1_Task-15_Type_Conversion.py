# Python Program to Demonstrate Type Conversion (int, float, str)

print("--- 1. Converting to Integer (int) ---")
num_str = "123"
num_float = 45.89

# Convert string to int
conv_int_1 = int(num_str)
# Convert float to int (Note: this truncates/removes the decimal portion, it does not round)
conv_int_2 = int(num_float)

print(f"Original string: '{num_str}' (Type: {type(num_str)})")
print(f"Converted to int: {conv_int_1} (Type: {type(conv_int_1)})\n")

print(f"Original float: {num_float} (Type: {type(num_float)})")
print(f"Converted to int: {conv_int_2} (Type: {type(conv_int_2)})\n")


print("--- 2. Converting to Float (float) ---")
num_str_decimal = "56.78"
num_int = 100

# Convert string to float
conv_float_1 = float(num_str_decimal)
# Convert int to float
conv_float_2 = float(num_int)

print(f"Original string: '{num_str_decimal}' (Type: {type(num_str_decimal)})")
print(f"Converted to float: {conv_float_1} (Type: {type(conv_float_1)})\n")

print(f"Original int: {num_int} (Type: {type(num_int)})")
print(f"Converted to float: {conv_float_2} (Type: {type(conv_float_2)})\n")


print("--- 3. Converting to String (str) ---")
age = 21
pi_val = 3.14159

# Convert int to string
conv_str_1 = str(age)
# Convert float to string
conv_str_2 = str(pi_val)

print(f"Original int: {age} (Type: {type(age)})")
print(f"Converted to string: '{conv_str_1}' (Type: {type(conv_str_1)})\n")

print(f"Original float: {pi_val} (Type: {type(pi_val)})")
print(f"Converted to string: '{conv_str_2}' (Type: {type(conv_str_2)})")