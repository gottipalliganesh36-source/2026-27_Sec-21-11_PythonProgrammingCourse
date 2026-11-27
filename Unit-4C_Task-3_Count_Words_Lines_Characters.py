filename = "Hello world.txt"

with open(filename, "r") as file:
    text = file.read()

line_count = len(text.split("\n"))
word_count = len(text.split())
char_count = len(text)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)