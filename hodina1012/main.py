xb = int(input("Zadej X souřadnici bodu: "))
yb = int(input("Zadej Y souřadnici bodu: "))
if xb >5 and xb <10 and yb >2 and yb <7:
    print("Panáček je v nebezpečí")
elif xb >=5 and xb <=10 and yb ==2 or yb == 7:
    print("Panáček je na okraji")
elif yb >= 2 and yb <=7 and xb == 10 or xb == 5:
    print("Panáček je na okraji")
else:
    print("Panáček je v bezpečí")