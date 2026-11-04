print("Mysli si číslo od 1 do 100, které pak budu muset uhodnout.")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    pokusy += 1
    tip = int(dole + nahore) // 2

    print(f"můj typ je: {tip}")
    odpoved = input("Je to správně?")

    if odpoved == "s":
        print("Děkuji za hru")
        print(f"Uhodl jsem číslo {tip} na {pokusy}. pokus.")
    elif odpoved == "v":
        dole = tip + 1.
    elif odpoved == "m":
        nahore = tip - 1.