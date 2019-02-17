import java.util.*;
import java.util.Stack;

public class ReverseString {

   public static void main (String[] args) {
      
      Scanner console = new Scanner(System.in);
      
         //create a Stack of ojects
      Stack<String> stack1 = new Stack<String>();
      
      String input, token;
      
      String [] tokenList;
      
         //input a sring
      System.out.print("Enter a string: ");
      input = console.nextLine();   
      
         //split the input ino the tokenList
      tokenList = input.split(" ");
      
         //pus each token into th estack
      for( int i = 0; i < tokenList.length; i++) {
         stack1.push( tokenList[i] );         
      }
      
         //print 
      System.out.println("\n\nin reverse order: ");
      
      while( !stack1.isEmpty() ) {
         System.out.print( stack1.pop() + " " );   
      }     
   }//end main
}//end of class