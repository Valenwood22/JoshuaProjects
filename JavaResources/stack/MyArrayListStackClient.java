import java.util.*;

//@SuppressWarnings("unchecked")

public class MyArrayListStackClient {

		
   public static void main(String[] args) {
   
      MyArrayListStack<String> bookStack = new MyArrayListStack<String>();
      
      bookStack.push("Java Book");
      bookStack.push("Fine Art");
      bookStack.push("Discrete Math");
      bookStack.push("Python Programing");
      
      System.out.println( bookStack );
   
      System.out.println("The top book is: " + bookStack.peek() );
      
      System.out.println("\nRemove the top object: " + bookStack.pop() );
      System.out.println("Remove the top object: " + bookStack.pop() + "\n");
      
      System.out.println( bookStack );
      
      
   }//end of main()

}//end of class













