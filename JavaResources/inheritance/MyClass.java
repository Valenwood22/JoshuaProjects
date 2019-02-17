
public class MyClass implements SomeInterface {
       
       //My Class must provide the code blocks for all the abstract methods
       //for all the abstract methods in SomeInterface
       
   public int getSum(int n1, int n2, int n3) {
      return n1 + n2 + n3;
   }
   
   public double getAverage(int x, int y) {
      return (x + y) / 2.0;
   }
   
   public void printMessage() {
      System.out.println("Hello World!");
   }
       
}//end class
