
import java.util.*;

public class Exception1
{
   static Scanner console = new Scanner(System.in);

   public static void main(String[] args)
   {
      int dividend, divisor, quotient, remainder;           
   
      try {
         System.out.print("Enter the dividend: ");            
         dividend = console.nextInt();              
                            
      
         System.out.print("Enter the divisor: ");             
         divisor = console.nextInt();               
                         
      
         quotient = dividend / divisor; 
         remainder = dividend % divisor;            
      
         System.out.println("\nQuotient = " + quotient);  
         System.out.println("Remainder = " + remainder);             
      }
      catch(InputMissmatchException e) {
         System.out.println( "Exception Message: " + e.toString() );
      }
      catch(ArithmeticException e) {
         System.out.println( "Exception Message: " + e.toString() );
      }
      catch(Exception e) {
         System.out.println( "Exception Message: " + e.toString() );
      }
      finally {
         System.out.println( "Done");
      }
   }
}

