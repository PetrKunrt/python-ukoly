# Číslo 1
# Číslo 2
# Číslo 3
# Číslo 4
# Číslo 5

# 1. Nastavení počáteční hodnoty řídící proměnné
pocitadlo = 1

# 2. Cyklus běží, dokud platí podmínka (dokud je počitadlo menší nebo rovno 5).
while pocitadlo <= 5:
    print(f"Číslo: {pocitadlo}")
    pocitadlo += 1 # Zvýšení hodnoty o 1 (důležité, aby cyklus neskončil v nekonečné smyčce).

print("Konec cyklu")
print(f"Číslo: {pocitadlo}")