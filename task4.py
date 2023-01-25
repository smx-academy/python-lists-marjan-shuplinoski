lista = []
for i in range(5):
    ime = input("Vnesi ime: ")
    lista.append(ime)

najdolgo_ime = max(lista, key=len)
print("Najdolgoto ime e {} od listata {}".format(najdolgo_ime, lista))
