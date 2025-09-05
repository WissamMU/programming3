# Read a, b
Sa = input("a=")
a = int(Sa)
Sb = input("b=")
b = int(Sb)
# Compute GCD of a and b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
g = a
print("GCD = " + str(g))
