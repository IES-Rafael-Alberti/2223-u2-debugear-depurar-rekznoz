
def algoritmo_burbuja(random):
    if not isinstance(random, list):
        raise ValueError("Solo se aceptan Listas")

    ordenada = random.copy()
    for i in range(len(ordenada) - 1):
        for j in range(len(ordenada) - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    return ordenada

if __name__ == "__main__":
    lista = [6, 8, 4, 82, 47, 47, 15, 65, 1, 97]
    lista_ordenada = algoritmo_burbuja(lista)

    print("Lista sin ordenadar ", lista)
    print("Lista ordenada ", lista_ordenada)
