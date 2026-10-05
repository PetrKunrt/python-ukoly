# Příkaz větvení
x = 5
a = x
if x > 0: 
    print("Kladné")
else:
    if (x<0):
        print("Záporné")
        a = -x
    else:
        print("Nula")
        # sem směřují skoky ze všech větví příkazů

print(f"Absolutní hodnota čísla {x} je {a}")


if x>0:
    print("KLadné")
elif x <0:
    print("Záporné")
    a = -x
else:
    print("Nula")


cislo = -50
kladne_cislo = cislo > 0
print(kladne_cislo)
