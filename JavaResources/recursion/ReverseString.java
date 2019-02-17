

import java.util.*;

public class ReverseString {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
      
      String s1;
      System.out.print("Enter a string: ");
      s1 = console.nextLine();
      
      printStringReverse( s1, 0, s1.length() );    
      
      
        
   }//end main
   
   public static void printStringReverse( String s1, int index, int size) {
   
      if( (size - index) == 1 ) {
         System.out.print(s1.charAt(index));          
      }
      else {
         printStringReverse( s1, index+1, size );
         System.out.print( s1.charAt(index) );
      }
   }      
}//end class