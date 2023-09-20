//1. Verificar si un número es positivo, negativo o cero.
package Java;
import java.util.Scanner;

public class numVerification {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        double numero = num.nextDouble();

        if(numero > 0){
            System.out.println("El numero es positivo.");
        } else if(numero < 0){
            System.out.println("El numero es negativo.");
        } else{
            System.out.println("El numero es cero.");
        }

        num.close();
    }
}