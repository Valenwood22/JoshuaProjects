
import java.util.*;

public class QuadraticEquation {
   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {

      int a, b, c;
      double discriminant;
      
      try{
         System.out.print("Enter a: ");
         a = console.nextInt();
         
         if( a == 0 ) {
            throw new ArithmeticException("a is 0,");
         }
         
         System.out.print("Enter b: ");
         b = console.nextInt();
         
         System.out.print("Enter c: ");
         c = console.nextInt();
         
         discriminant = calculateDiscriminant( a, b, c);
         
         calculateAndPrintRoot( a, b, c, discriminant );

      }
      catch(InputMismatchException e) {
         System.out.println("Enter integers for a, b, and c.");
      }
      catch(ArithmeticException e) {
         System.out.println( e.toString() );
      }
      catch(Exception e) {
         System.out.println("The equation has complex roots.");
      }   
               
   }//end main
   
   public static double calculateDiscriminant( int a, int b, int c) {
      return b * b - 4.0 * a * c;
   }
   
   public static void calculateAndPrintRoot(int a, int b, int c, double discriminant) throws Exception {
   
      double root1, root2;
      
      if(discriminant == 0) {
         root1 = root2 = -b / (2*a);
         
         System.out.println("Single root: " + root1);
      }
      else if( discriminant > 0) {
         root1 = (-b + Math.sqrt(discriminant) ) / (2*a);
         root2 = (-b - Math.sqrt(discriminant) ) / (2*a);
         
         System.out.println("Root 1: " + root1);
         System.out.println("Root 2: " + root2);

      }
      else {

         throw new Exception("Discriminant is less than 0.");

      }
   }
   
}//end class