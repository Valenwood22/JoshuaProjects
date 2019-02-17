
import java.util.*;

public class SumArray {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      int [] list = {5, 8, 10, 4, 2};
      int total;
      
      total = calTotal( list, list.length );
      
      System.out.println("Sum: " + total);
  
   }//end main
   
   public static int calTotal( int [] list, int n) {
  
      if( n == 1 ) {
         return list[0];
      }
      else {
         return calTotal(list, n-1) + list[ n-1 ];
      }    
   }
}//end class