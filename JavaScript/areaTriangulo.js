const prompt = require("prompt-sync")()
//1. Calcular el área de un triángulo.
//Lados del triángulo 
const ladoA = parseFloat(prompt("Ingrese el valor del lado A: "));
const ladoB = parseFloat(prompt("Ingrese el valor del lado B: "));
const ladoC = parseFloat(prompt("Ingrese el valor del lado C: "));

//Semiperimetos
const s = (ladoA + ladoB + ladoC) / 2;

//Área
const area = Math.sqrt(s*(s-ladoA)*(s-ladoB)*(s-ladoC))

//Imprimir área
console.log(`El area del triangulo es: ${area}`);
