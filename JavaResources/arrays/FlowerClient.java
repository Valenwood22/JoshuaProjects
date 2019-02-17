/*
*
*
*
*/

import java.util.*;
import java.util.ArrayList;

public class FlowerClient {

   static final int SIZE = 3;

   public static void main(String [] args) {
      Scanner console = new Scanner(System.in);
   	
         //cretae an ArrayList object
      ArrayList<Flower> flowerList = new ArrayList<Flower>();
      
      for(int i=0; i<SIZE; i++){
         System.out.println("\n\nEnter the information for the Flower " + (i+1));
         
         System.out.print("\nEnter name: ");
         String name = console.next();
         
         System.out.print("\nEnter pedals: ");
         int pedals = console.nextInt();
         
         System.out.print("\nEnter cost: ");
         double cost = console.nextDouble();
      
            //create a Flower object and add it to the flowerList
         flowerList.add( new Flower(name, pedals, cost) );
      } 
      
      //output
      for(int i=0; i<flowerList.size(); i++) {
         System.out.println( flowerList.get(i) );
      }
      
      //find the index of the most expensive flower
      int maxIndex =0;
      
      for(int i=0; i<flowerList.size(); i++) {
      
         if( flowerList.get(i).getPrice() > flowerList.get(maxIndex).getPrice() ) {
            maxIndex = i;
         } 
         
      }
      
      System.out.println("The most expensive flower is " + flowerList.get(maxIndex).getName() );
      
         //use set method to replace a flower
      Flower replaced = flowerList.set( 1, new Flower( "Sun Flower", 25, 4.99) );
      
      System.out.println("Replaced flower; " +replaced );
      
         //remove the first flower (index0)
      System.out.println("Remove flower: "+ flowerList.remove(0) );
     
         //print the array list again
      for(int i=0; i<flowerList.size(); i++) {
         System.out.println( flowerList.get(i) );
      }              
      
   }//end main   
   
}//end class