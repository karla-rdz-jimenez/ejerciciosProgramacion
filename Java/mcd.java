//3. Encontrar el máximo común divisor de dos números.
package Java;
import java.util.Scanner;

public class mcd {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.println("Ingrese el primer numero: ");
        int num1 = num.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        int num2 = num.nextInt();

        int maxComDiv = calculo(num1, num2);
        System.out.println("El maximo comun divisor de " + num1 + " y " + num2 + " es: " + maxComDiv);
        
        num.close();
    }

    public static int calculo(int a, int b){
        if(b == 0){
            return a;
        }
        return calculo(b, a%b);
    }
}
