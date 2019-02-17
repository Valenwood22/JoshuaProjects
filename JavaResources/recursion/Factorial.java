
import java.util.*;

public class Factorial {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      int n, answer;
      
      System.out.print("Enter n: ");
      n = console.nextInt();
      
      answer = calFactorial( n );
      
      System.out.println( n + "! = " + answer);
       
   }//end main
   
   public static int calFactorial( int n ) {
   
      if( n == 1 ) {
         return 1;
      }
      else {
         return n * calFactorial( n - 1);
      }
   }
   
}//end class

