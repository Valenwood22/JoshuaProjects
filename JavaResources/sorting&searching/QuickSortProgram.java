import java.util.*;

public class QuickSortProgram {

   public static void main(String [] args) {
   
      Scanner console = new Scanner(System.in);
   	  
      Random rand = new Random();
   	  
      int [] list = new int[25];
   
      for (int i = 0; i < list.length; i++) {
            //list[i] = (int)(Math.random() * 500 +1);
         list[i] = rand.nextInt(500) + 1;    //0 to 499, 1 to 500
      }
   	  
      System.out.println("\nAll Elements:");
      printArray( list ); 
      
         //call quick sort method
      quickSort( list, 0, list.length-1);
      
      System.out.println("\nAfter calling quick sort method, all elements:");
      printArray( list );
         
   }//end main

   public static void printArray(int[] list) {
      for (int i = 0; i < list.length; i++) {
         System.out.print(list[i] + " ");
      }
   }
      //quick sort method
   public static void quickSort(int [] list, int left, int right) {
      if(left < right) {
         int q = partition( list, left, right );
         quickSort( list, left, q);
         quickSort( list, q+1, right);
      }
   }   
   
      //partition method
   public static int partition( int [] list, int left, int right) {
      
      int x = list[left]; //piviot
      int i = left - 1;
      int j = right + 1;
      
      
      while(true) {
      
         j--;
         while(list[j] > x) {
            j--;
         }
      
         i++;
         while(list[i] < x) {
            i++;
         }
         
         if(i < j ){
            int temp = list[j];
            list[j] = list[i];
            list[i] = temp;
         }
         else {
            return j;
         }   
      
      }//end while
      
   }//end partation  

} //end class