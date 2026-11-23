# Vykreslování obrazců hvězdiček

def ctverec(strana):
    i = int(input("Zadej velikost strany: "))
    radek = 0
    while radek < strana:
        print("*" * strana)
        radek += 1

def ctverec_duty(strana):
    i = int(input("Zadej velikost strany: "))
    radek = 0
    while radek < strana:
        if radek == 0 or radek == strana - 1:
            print("*" * strana)
        else:
            print("*" + " " * (strana - 2) + "*") 
        radek += 1

def obdelnik():
    a = int(input("Zadej velikost strany a: "))
    b = int(input("Zadej velikost strany b: "))
    radek = 0
    while radek < b:
        print("*" * a)
        radek += 1

pokracovat = True
while pokracovat:
    volba = input("Jaký obrazec chceš nakreslit? [c, cn, o]")
    if volba == "c":
        ctverec()
    elif volba == "cn":
        ctverec_duty()
    elif volba == "o":
        obdelnik()
    else:
        print("Neplatný výběr! Vyber z [c, cn, o]")
    odpoved = input("Chceš vykreslit další obrazec? [ano/ne]")
    if odpoved != "ano":
        pokracovat = False
print("Děkuji za použití programu")