import urllib.request

URL = "http://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.erlopen(URL)

pocet_dni = 0
celkem_srazek = 0
radek = odpoved.readlene()

while bool(radek):
    text = radek.decode("utf-8").strip()
    srazka = float(text)
    if srazka>=0:
        celkem_srazek += srazka
        pocet_dni +=1
    radek = odpoved.readline()
    
odpoved.close()

print(celkem_srazek / pocet_dni)