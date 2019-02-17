import java.util.*;

public class ArrayProcessing
{
   public static void main(String [] args)
   {
      Scanner console = new Scanner(System.in);
   	  
      Random rand = new Random();
   	  
      int [] list = new int[25];
   
      for (int i = 0; i < list.length; i++)
      {
            //list[i] = (int)(Math.random() * 500 +1);
         list[i] = rand.nextInt(500) + 1;    //0 to 499, 1 to 500
      }
   	  
      System.out.println("\nAll Elements:");
      printArray( list );
      
         //call average method
      System.out.println();
      System.out.printf("The Average value is %.2f", average( list ) );
      
         //call indexOfSmallest method
      int minIndex = indexOfSmallest( list );
         
      System.out.println();
      System.out.println("The smallest value " + list[minIndex] + " is at index " + minIndex );
      
        //call countEven
      System.out.println("Number of evem elements is " + countEven(list) );   
      
      
   }

   public static void printArray(int[] list)
   {
      for (int i = 0; i < list.length; i++)
         System.out.print(list[i] + " ");
   }
   
   
      //calculate and return the average vlue of array elements
   public static double average( int [] list ) {
      
      int sum = 0;
      
      for (int i=0; i < list.length; i++) {
         sum += list[i];
      }
      
      return sum / (double)list.length;
   
   }
   
      //find the index of the smallest value in the array
   public static int indexOfSmallest( int [] list ) {
      
      int minIndex = 0;
      
      for (int i=0; i < list.length; i++) {
      
         if( list[i] < list[minIndex] ) {
            minIndex = i;  
         }
      }
      return minIndex;
   }    
   
      //count the number of even elements in the array
   public static int  countEven( int [] list ) {
      
      int evenCount = 0;
      
      for(int i=0; i<list.length; i++) {
         if( list[i] % 2 == 0) {
            evenCount++;
         }
      }
      return evenCount; 
   }   
   
}
