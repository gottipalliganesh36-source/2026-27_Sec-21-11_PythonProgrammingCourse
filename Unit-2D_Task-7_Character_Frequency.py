s = input("Enter a string: ")

frequency = {}  # empty dictionary {}

for ch in s:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for char, count in frequency.items():
    print(char, ":", count)