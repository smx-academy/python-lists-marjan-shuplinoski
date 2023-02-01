lista = []

for i in range(5):
    broj = int(input("Vnesi broj: "))
    lista.append(broj)

lista.sort()
najgolem_broj = lista[-1]
vtor_najgolem_broj = lista[-2]

print("Najgolemiot broj e {}, vtor najgolem e {} od listata {}".format(najgolem_broj,vtor_najgolem_broj, lista))
