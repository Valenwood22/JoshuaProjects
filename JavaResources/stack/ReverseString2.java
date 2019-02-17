import java.util.*;
import java.util.Stack;

public class ReverseString2 {

   public static void main (String[] args) {
      
      Scanner console = new Scanner(System.in);
      
         //create a Stack of ojects
      Stack<String> stack1 = new Stack<String>();
      
      Stack<Character> stack2 = new Stack<Character>();
      
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
      System.out.println("\nin reverse order: ");
      
      while( !stack1.isEmpty() ) {
         
         token = stack1.pop();
         
            //push each letter in tolen into stack2
         for( int i=0; i<token.length(); i++) {
            stack2.push( token.charAt(i) );
         }
            //pop each letter from stck2 
         while( !stack2.isEmpty() ) {
            System.out.print( stack2.pop() );
         }            
         
         System.out.print(" ");
         
      } 
   }//end main
}//end of class