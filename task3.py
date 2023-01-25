lista = []

for i in range(5):
    element = int(input("Vnesi nekoj element: "))
    lista.append(element)

print("Listata e {}".format(lista))
pocetok = int(input("Vnesete od koj indeks da se brisi: "))
kraj = int(input("Vnesete do koj indeks da se brisi: "))

del lista[pocetok:kraj]
print("Brisenjeto e uspesno eve ja novata lista {}".format(lista))