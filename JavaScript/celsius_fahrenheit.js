const prompt = require("prompt-sync")()
//2. Convertir grados Celsius a Fahrenheit.
//Temperatura en Celsius
const tempCelsius = parseFloat(prompt("Ingrese la temperatura en grados Celsius: "));

//Conversión a Fahrenheit: Grados Fahrenheit = (grados centígrados × 9/5) +32.
const tempFahrenheit = (tempCelsius * 9/5)+32;

//Imprimir resultado
console.log(`${tempCelsius} grados Celsius equivalen a ${tempFahrenheit} grados Fahrenheit.`);
