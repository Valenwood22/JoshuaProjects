/*
 *
 *
 *
 *
 */
 import java.util.Scanner;
 
public class Josephus {
   
   static final int SIZE =41;
 
   static Scanner console = new Scanner(System.in);
   
   public static void main(String[] args) {
      
      int skip, targetIndex;
      
      MyArrayList<String> soldierList = new MyArrayList<String>();
      
         //load 41 soldiers to the array list
      for(int i=0; i<SIZE; i++) {
         soldierList.add(i, "Soldier " + (i+1) );
      }  
      
         //print the soldierlist
      System.out.println( soldierList.toString() );
      
      System.out.print("Enter the number of soldiers to skip: ");
      skip = console.nextInt();
      
      //treating the list as a circular list, remove every n'th soldier
      //until the list is empty
      targetIndex = skip;
      
      while( !soldierList.isEmpty() ) {
         
         System.out.println( soldierList.remove( targetIndex ) + " is removed." );
         if( soldierList.size() > 0 ) {
         targetIndex = (targetIndex + skip) % soldierList.size();
         }
         
      }

   }
}























