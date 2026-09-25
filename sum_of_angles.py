a = int(input("enter the angle:"))
b = int(input("enter the angle:"))
c = int(input("enter the angle:"))
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("valid triangle")
else:
    print("Not a valid triangle")