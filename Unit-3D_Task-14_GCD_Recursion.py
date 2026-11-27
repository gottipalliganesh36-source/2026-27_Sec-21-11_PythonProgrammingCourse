def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)  # recursive call

x, y = 48, 18
print("GCD:", gcd(x, y))