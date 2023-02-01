lista_produkti = []
lista_ceni = []
while True:
    produkt = input("Vnesi produkt: ")
    lista_produkti.append(produkt)
    cena = int(input("Vnesi cena: "))
    lista_ceni.append(cena)
    da_ne = input("Ke plakjate? (da/ne) ")
    if (da_ne == "da"):
        break;

for i in range(len(lista_produkti)):
    print("Produkt: {} Cena: {}".format(lista_produkti[i], lista_ceni[i]))

vkupno = sum(lista_ceni)
print("Vkupno dolzite: {}".format(vkupno))
da_ne_plakanje = input("Dali ke plakjate? (da/ne)")
if (da_ne_plakanje == "da"):
    plakanje = int(input("Vnesete ja vasata uplata: "))
    if (plakanje < vkupno):
        plakanje = int(input("Ve molime uplatete poveke: "))
        kusur = plakanje - vkupno
    else:
        kusur = plakanje - vkupno
else:
    print("Vratete gi proizvodite")

print("Vasiot kusur e {}".format(kusur))