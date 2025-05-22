"""1. Ejercicio básico de Python (Nivel Principiante)
Enunciado: Crea una función llamada numero_mas_frecuente(lista) que reciba una lista de
números enteros y devuelva el número que más veces se repite. Si hay más de uno con la
misma frecuencia, devuelve el menor de ellos.
Ejemplo:
numero_mas_frecuente([1, 3, 1, 3, 2, 1]) # Resultado esperado: 1
numero_mas_frecuente([4, 4, 5, 5]) # Resultado esperado: 4"""


def numero_mas_frecuente(lista):
    max_frecuencia = 0
    num_mas_frecuente_encontrado = None 

    for num in lista:
        frecuencia = lista.count(num)

        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            num_mas_frecuente_encontrado = num
        elif frecuencia == max_frecuencia: 
            if num_mas_frecuente_encontrado is None:
                num_mas_frecuente_encontrado = num
            elif num < num_mas_frecuente_encontrado:
                num_mas_frecuente_encontrado = num
    return num_mas_frecuente_encontrado


print(numero_mas_frecuente([1, 3, 1, 3, 2, 1]))
print(numero_mas_frecuente([4, 4, 5, 5]))
print(numero_mas_frecuente([1, 3, 1, 3, 2, 3, 3]))
print(numero_mas_frecuente([10, 20, 10, 30, 20, 20]))
print(numero_mas_frecuente([]))