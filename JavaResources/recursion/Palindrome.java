
import java.util.*;

public class Palindrome {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      String s1 = "Able was I ere I saw Elba";
      String s2 = "Now is the time for all good men";
     
      if( isPalindrome(s1.toUpperCase() ) ) {
         System.out.println("Yes");
      }
      else {
         System.out.println("No");
      }
     
   }//end main
   
   public static boolean isPalindrome( String s ) {
   
      boolean status = false;
      
      if(s.length() <= 1) {  //only one letter
         status = true;
      }
      else if(s.charAt(0) == s.charAt( s.length()-1) ){
         status = isPalindrome( s.substring(1, s.length()-1) );
      }
      
      return status; 
   }   
        
}//end class

