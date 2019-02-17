import java.util.*;

public class SortingAndSearchingPrimitive {

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
      
         //call selection sort method
      selectionSort( list );
      
      System.out.println("\n\nAll Elements:");
      printArray( list );
      
         //binary search
      System.out.print("\n\nEnter a key to search: ");
      int key = console.nextInt();   
           
      int foundIndex = binarySearchRecursion( list, 0, list.length-1, key );
      
      if(foundIndex == -1) {
         System.out.println("Not Found");
      }
      else {
         System.out.println("Found at index " + foundIndex);
      }
      
   }//end main

   public static void printArray(int[] list) {
      for (int i = 0; i < list.length; i++) {
         System.out.print(list[i] + " ");
      }
   }
   
      //selection sort method
   public static void selectionSort( int [] list ) {
   
      int minIndex, temp;
      
      for(int x=0; x<list.length-1; x++) {

         minIndex=x;
         
         for(int i=x+1; i<list.length; i++) {
            if(list[i] < list[minIndex]) {
               minIndex = i;
            }
         }
      
         //swap
         temp = list[x];
         list[x] = list[minIndex];
         list[minIndex] = temp;   
      
      }
   }
   
      //binary search method
   public static int binarySearchRecursion( int [] list, int leftIndex, int rightIndex, int key) {
   
      int middle = (leftIndex + rightIndex) / 2;
      
      int foundIndex = -1;
      
      if(list[middle] == key) {
         foundIndex = middle; //found it
      }
      else if( key < list[middle] ) {
         if( leftIndex <= list[middle] ) {
            foundIndex = binarySearchRecursion( list, leftIndex, middle-1, key); //recurstion
         }
      }
      else{
         if( rightIndex >= middle+1) {
            foundIndex = binarySearchRecursion( list, middle+1, rightIndex, key); //recursion
         }
      }
      
      
      return foundIndex;
   }
   
} //end class