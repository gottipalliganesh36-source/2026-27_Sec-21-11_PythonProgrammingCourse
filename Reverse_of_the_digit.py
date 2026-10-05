number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:  # continue while number still has digits
    digit = number % 10  # get the last digit with % 10
    reversed_number = reversed_number * 10 + digit  # build reverse
    number = number // 10  # remove the last digit with // 10
print(f"Reverse of {original_number} is {reversed_number}")