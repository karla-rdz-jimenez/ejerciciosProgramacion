# 1. Ordenar una lista de números de forma ascendente

#Para ingresar los números desde el teclado:
print("Ingrese los números, separados por comas, que serán parte de la lista:")
teclado = input()
print("Los números que ingresaste son: ", teclado)

#Dividir la cadena en "mini cadenas"
numeros = teclado.split(',')
#Convertir las "mini cadenas" en números enteros
numerosEnteros = [int(num) for num in numeros]

#Ordenarmiento de forma ascendente
numerosOrdenados = sorted(numerosEnteros)

#Imprimir la lista ya ordenada
print("Los numeros ordenados de forma ascendente: ", numerosOrdenados)