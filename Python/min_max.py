#2. Encontrar el mínimo y máximo de una lista de números

print("Ingrese los números, separados por comas, que serán parte de la lista:")
teclado = input()
print("Los números que ingresaste son: ", teclado)

#Dividir la cadena en "mini cadenas"
numeros = teclado.split(',')
#Convertir las "mini cadenas" en números enteros
numerosEnteros = [int(num) for num in numeros]

#Encontrar el Mínimo y el Máximo
minimo = min(numerosEnteros)
maximo = max(numerosEnteros)

print("El número mínimo es: ", minimo)
print("El número máximo es: ", maximo)