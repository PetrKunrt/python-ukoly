import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 0
max_pokusy = 5

print("Myslím si číslo od 1 do 20. Hádej mé číslo na pět pokusů!")

while tip != tajne_cislo and pokusy<max_pokusy:
    tip = int(input("Zadej sůj tip: "))
    pokusy += 1
    if tip > tajne_cislo:
        print("Tajné číslo je menší.")
    elif tip<tajne_cislo:
        print("Tajné číslo je větší.")

if tip == tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
else:
    print(f"Bohužel ti došly pokusy! Moje tajné číslo bylo {tajne_cislo}")