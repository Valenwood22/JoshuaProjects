
import java.util.*;

public class YouthLeague {
   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
         
         //declare variables
      int age;           
      
      
      while(true) {
         System.out.print("Enter an age (between 12 and 18): ");
      
         try {
            age = console.nextInt();

            if(age <= 0 ) {
               throw new Exception("n");
            }
            else if( age < 12 ) {
               throw new Exception("y");
            }
            else if( age > 18) {
               throw new Exception("o");       
            }
            
            System.out.println("Welcome to the youth league.");
            
            break;
         
         }
         catch(InputMismatchException e) {
            console.next();
            
            System.out.println( "Invalid input, enter an integer between 12 and 18." );    
         }
         catch(Exception e) {
            System.out.println( e.toString() );
         
            char errorCode = e.toString().charAt( e.toString().length() -1 );
         
            if( errorCode == 'n' ) {
               System.out.println("Age must be greater than zero");
            }
            if( errorCode == 'y' ) {
               System.out.println("Too young to join the youth league.");
            }
            if( errorCode == 'o' ) {
               System.out.println("Too old to join the youth league.");
            }
         }
         
      }//end while
      
   }//end main
}//end class

