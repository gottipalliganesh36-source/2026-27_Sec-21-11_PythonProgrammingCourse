num = int(input("Enter a 3 digit number:"))
orig_num = num
total = 0
while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10
    print(f"(orig_num) is an armstrong number")
else:
    print(f"(orig_num) is not an armstrong number")