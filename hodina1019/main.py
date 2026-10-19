a = int(input("zadej číslo a"))
b = int(input("zadej číslo b"))
c = int(input("zadej číslo c"))

if a>b:
    p = a
    a = b
    b = p
if b>c:
    p = b
    b = c
    c = p
if a>b:
    p = a
    a = b
    b = p
print(f"{a}, {b}, {c}")