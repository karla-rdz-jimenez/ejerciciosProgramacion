//2. Calcular el promedio de un arreglo de números. 
package Java;
import java.util.Scanner;

public class promedio {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de numeros qu tendrá el arreglo de numeros:");
        int n = num.nextInt();

        double[] numeros = new double[n];

        for(int i=0; i<n; i++){
            System.out.println("Ingrese el numero " + (i+1)+ ": ");
            numeros[i] = num.nextDouble();
        }

        double sum = 0;

        for(double numero: numeros){
            sum += numero;
        }

        double prom = sum / n;

        System.out.println("El promedio de los numeros que ingresaste es: " + prom);

        num.close();

    }
}
