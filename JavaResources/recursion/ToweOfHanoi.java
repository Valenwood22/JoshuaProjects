
import java.util.*;

public class ToweOfHanoi {

   static Scanner console = new Scanner(System.in);

   public static void main(String[] args) {
   
      int n;
      
      System.out.print("Enter the number of disks: ");
      n=console.nextInt();
      
      moveDisks( n, 1, 3, 2 );
       
   }//end main
   
   public static void moveDisks( int n, int tower1, int tower3, int tower2 ) {
      
         //base case
      if( n == 1 ) {
         System.out.printf( "Move a disk from %d to %d %n", tower1, tower3 );
      }   
      else {
          moveDisks( n-1, tower1, tower2, tower3 );
          System.out.printf( "Move a disk from %d to %d %n", tower1, tower3 );
          moveDisks( n-1, tower2, tower3, tower1 );
      }
   }
}//end class