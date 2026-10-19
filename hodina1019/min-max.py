a = int(input("zadej číslo a "))
b = int(input("zadej číslo b "))
c = int(input("zadej číslo c "))

min = a
max = a

if b<min:
    min = b
elif b>max:
    max = b

if c<min:
    min = c
elif c>max:
    max = c

print(f"minimum = {min} maximum = {max}")