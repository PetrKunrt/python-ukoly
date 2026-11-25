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

def obdelnik_duty():
    a = int(input("Zadej velikost strany a: "))
    b = int(input("Zadej velikost strany b: "))
    radek = 0
    while radek < b:
        if radek == 0 or radek == b - 1:
            print("*" * a)
        else:
            print("*" + " " * (a - 2) + "*") 
        radek += 1

def pravo_troj():
    strana = int(input("Zadej velikost strany: "))
    troj_strana = 1
    radek = 0
    while radek < strana:
        print("*" * troj_strana)
        radek += 1
        troj_strana += 1

def pravo_pravo_troj():
    strana = int(input("Zadej velikost strany: "))
    troj_mezera = strana
    troj_strana = 1
    radek = 0
    while radek < strana:
        print(" " * troj_mezera + "*" * troj_strana)
        radek += 1
        troj_mezera -= 1
        troj_strana += 1

def troj_lichy():
    strana = int(input("Zadej velikost základny: "))
    troj_mezera = strana // 2
    troj_strana = 1
    radek = 0
    vyska = (strana + 1) // 2
    
    while radek < vyska:
        print(" " * troj_mezera + "*" * troj_strana + " " * troj_mezera)
        radek += 1
        troj_mezera -= 1
        troj_strana += 2

def troj_sudy():
    strana = int(input("Zadej velikost základny: "))
    vyska = strana // 2
    troj_mezera = vyska - 1
    troj_strana = 1
    radek = 0
    
    while radek < vyska:
        print(" " * troj_mezera + "**" * troj_strana + " " * troj_mezera)
        radek += 1
        troj_mezera -= 1
        troj_strana += 1

pokracovat = True
while pokracovat:
    volba = input("Jaký obrazec chceš nakreslit? [c, cn, o, on, pt, ppt, tl, ts]")
    if volba == "c":
        ctverec()
    elif volba == "cn":
        ctverec_duty()
    elif volba == "o":
        obdelnik()
    elif volba == "on":
        obdelnik_duty()
    elif volba == "pt":
        pravo_troj()
    elif volba == "ppt":
        pravo_pravo_troj()
    elif volba == "tl":
        troj_lichy()
    elif volba == "ts":
        troj_lichy()
    else:
        print("Neplatný výběr! Vyber z [c, cn, o, on, pt, ppt, tl, ts]")
    odpoved = input("Chceš vykreslit další obrazec? [ano/ne]")
    if odpoved != "ano":
        pokracovat = False
print("Děkuji za použití programu")