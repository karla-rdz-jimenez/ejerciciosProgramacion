const prompt = require("prompt-sync")()
//3. Encontrar el máximo de dos números.
//Ingresar los 2 números
const num1 = parseFloat(prompt("Ingrese el primer numero: "));
const num2 = parseFloat(prompt("Ingrese el segundo numero: "));

//Compararción entre los números
if(num1 > num2){
    console.log(`El número máximo es: ${num1}`);
}else if(num1 < num2){
    console.log(`El número máximo es: ${num2}`);
}else{
    console.log(`Los numeros son iguales.`);
}
