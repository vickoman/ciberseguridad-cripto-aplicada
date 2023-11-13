# Get values from input
a = int(input("a: "))
b = int(input("b: "))

# Accept two numbers and return the greatest common divisor and extend theirs 
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


print("GDC:", extended_gcd(a, b))
