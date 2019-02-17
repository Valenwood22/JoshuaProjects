
import java.util.*;

public class GCD {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      int m, n, result;
      
      System.out.print("enter m and n: ");
      m=console.nextInt();
      n=console.nextInt();
      
      result = caculateGCD( m, n);
      
      System.out.println("GCD: " + result);
       
   }//end main
   
   public static int caculateGCD( int m, int n) {
      
      int r;
      r = m%n;
      if( r == 0 ) {
         return n;
      }
      else {
         return caculateGCD( n, r );
      }
   }
}//end class

