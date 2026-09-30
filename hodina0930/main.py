# ***********************
# Kalkulačka spropitného
#30.9.2026
# ***********************

print("Kalkulačka spropitného")    # titulní text
celkova_cena = input("Zadej celkovou cennu: ")
celkova_cena = float(celkova_cena)
spropitne = int(input("Zadej spropitné v %: "))
pocet_lidi = int(input("Zadej počet lidí: "))

# celkova_cena = celkova_cena + celkova_cena * spropitne / 100  # aritm. operace: +, -, *, /
# celkova_cena = celkova_cena * (1 + spropitne / 100)
celkova_cena += celkova_cena * spropitne / 100
uhradit = celkova_cena / pocet_lidi

# výstup
print(f"Celkova cena {celkova_cena} dělená {pocet_lidi} je {uhradit} Kč")