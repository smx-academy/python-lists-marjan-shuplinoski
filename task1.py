lista = []
for i in range(10):
    broj = int(input("Vnesi broj : "))
    lista.append(broj)
zbir = sum(lista)
print("site broevi se {} i nivniot zbir iznesuva {}".format(lista, zbir))
