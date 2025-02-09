def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo:

lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)
