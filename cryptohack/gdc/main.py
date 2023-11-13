# Get values from input
a = int(input("a: "))
b = int(input("b: "))
# Accept two numbers and return the greatest common divisor
def gdc(a, b):
    if b == 0:
        return a
    return gdc(b, a % b)

print("GDC:", gdc(a, b))
