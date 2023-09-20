# 3. Encontrar el segundo elemento más grande en una lista

#Para ingresar los números desde el teclado:
print("Ingrese los números, separados por comas, que serán parte de la lista:")
teclado = input()
print("Los números que ingresaste son: ", teclado)

#Dividir la cadena en "mini cadenas"
numeros = teclado.split(',')
#Convertir las "mini cadenas" en números enteros
numerosEnteros = [int(num) for num in numeros]

# Encontrar el segundo elemento más grande
if len(numerosEnteros) < 2:
    print("Se necesitan al menos 2 elementos para encontrar el segundo más grande.")
else:
   # Encontrar el segundo máximo
    maximo = max(numerosEnteros)
    #Se elimina el primer número más grande de la lista
    numerosEnteros.remove(maximo)
    #Se busca ahora el más máximo de la lista nueva
    segundoGrande = max(numerosEnteros)
    print("El segundo elemento más grande es:", segundoGrande)