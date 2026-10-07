# hra test to, nebo to
doprava = input("Přišel jsi na nádraží, pojedeš vlakem, nebo autobusem. (Autobus/Vlak)")
if doprava == "Autobus":
    print("Atobusem si dojel do školy v pohodě. Jen na malé vetlačení na začátku. Test z matiky si bohužel stihl.")
elif doprava == "Vlak":
    print("Vlak měl jako vždy spoždění, nestihl jsi spoj na hlaváku.")
    spozdeni = input("Cheš jít pro spožděnku, nebo jít radši hned na autobus. (Spožděnka/Hned jít)")
    if spozdeni == "Spožděnka":
        print("Autobus, kterým si měl jet si nestihl. Test po té taky né.")
    elif spozdeni == "Hned jít":
        print("Autobus dojel v čas, do hodiny si přišel na rozdávání testu.")
    else:
        print("Napiš to co je v nabítce")