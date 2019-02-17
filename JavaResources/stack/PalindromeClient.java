import java.util.*;
import java.util.Stack;

public class PalindromeClient {

   public static void main (String[] args) {
      
      Scanner console = new Scanner(System.in);
         
         //create a Stack object
      Stack<Character> stack1 = new Stack<Character>();
      Stack<Character> stack2 = new Stack<Character>();
      
      String input;
      
      System.out.print("Enter a string: ");
      input = console.nextLine();
      
      input = input.replaceAll("\\W", ""); //remove the white spaces and punctuations
      
      input = input.toUpperCase(); 
      
         //push each letter to the stack1 from the left to the right
      for(int i=0; i<input.length(); i++) {
         stack1.push( input.charAt(i) );
      }   
      
         //push each letter to stach2 from the right to the left
      for(int i= input.length()-1; i>=0; i--) {
         stack2.push( input.charAt(i) );
      
      }   
      
         //call the method to evaluate 
      boolean flag = evaluate( stack1, stack2);
      
      if(flag){
         System.out.println("Yes, it is a panlindrome.");
      }
      else {
         System.out.println("No, it i not a palindrome.");
      }
              
   }//end main()
   
   public static boolean evaluate( Stack stack1, Stack stack2 ) {
   
      while( !stack1.isEmpty() ) {
         
         if( stack1.pop() != stack2.pop() ) {
         
            return false;
         }
      } 
   
      return true;
   }
     
}//end of class