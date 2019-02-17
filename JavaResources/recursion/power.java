
import java.util.*;

public class power {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      int base, exponent, answer;
      
      System.out.print("enter base: ");
      base = console.nextInt();
      
      System.out.print("Enter exponent: ");
      exponent = console.nextInt();
      
      answer = power(base, exponent);
      
      System.out.println("Answer = " + answer);
      
   }//end amin
   
   public static int power( int b, int e ) {
      
      if( e == 1 ) {
         return b;
      }
      if( e == 0 ) {
         return 1;
      }   
      return b * power( b, e-1);
        
   }
}//end class