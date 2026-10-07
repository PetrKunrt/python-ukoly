hodina = input("Zadej kolik je: ")
hodina = float(hodina)

if hodina < 0:
    print("Hodina nemůže být záporná.")
elif hodina >= 24:
    print("Zadávejte platné hodiny.")
elif hodina < 6:
    print("Noc")
elif hodina < 9:
    print("Ráno")
elif hodina < 12:
    print("Dopoledne")
elif hodina < 13:
    print("Poledne")
elif hodina < 18:
    print("Odpoledne")
elif hodina < 21:
    print("Večer")
else:
    print("Noc")