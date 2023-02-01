lista = []
for i in range(5):
    broj = int(input("Vnesi broj: "))
    lista.append(broj)

najgolem_broj = max(lista)
print("Najgolemiot broj e {} od listata {}".format(najgolem_broj, lista))
