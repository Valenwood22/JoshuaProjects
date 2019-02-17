import java.util.*;

public class PostFixClient {

   public static void main (String[] args) {
      
      Scanner console = new Scanner(System.in);
         
         //create a MyArrayListStack object
      MyArrayListStack<Integer> intStack = new MyArrayListStack<Integer>();
      
         //declare varabels
      String expression, token;   
      
      int operand1, operand2, result = 0;
      
      String [] tokenList;
         
         //input
      System.out.println("Enter a valid postfix exprssion with a space between each token(ex 3 4 * 2 5 + - 4 * 2 / ): ");
      
      expression = console.nextLine();     
         
      tokenList = expression.split( " " );
      
      for(int i=0; i<tokenList.length; i++) {
         
         token = tokenList[i];
         
         if( token.equals("+") ||
             token.equals("-") ||
             token.equals("*") ||
             token.equals("/") ) { //operand
               
            operand2 = intStack.pop();
            operand1 = intStack.pop();
             
               //calcualte the result
            result = calculate( operand1, operand2, token);
            
            intStack.push(result);   
         
         
         }
         else {    //operand
            
            intStack.push( Integer.parseInt(token) );
         }
      }//end for loop
      System.out.println("Answer = " + result);
      
   }// end main()
   
   public static int calculate( int operand1, int operand2, String operator) {
   
      int answer =0;
      
      switch (operator) {
      
         case "+":
            answer = operand1+operand2;
            break;
         case "-":
            answer = operand1-operand2;
            break;
         case "*":
            answer = operand1*operand2;
            break;
         case "/":
            answer = operand1/operand2;
            break;      
      }
      
      return answer;
      
      
   }
   
     
}//end of class













