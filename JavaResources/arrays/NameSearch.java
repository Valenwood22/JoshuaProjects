/*
*
*
*
*/

import java.util.*;
import java.util.ArrayList;
import java.io.*;

public class NameSearch {

   static final int SIZE = 3;

   public static void main(String [] args) throws IOException {
   
      Scanner console = new Scanner(System.in);
      
         //create an ArrayList for the girl names
      ArrayList<String> girlNameList = new ArrayList<String>();
         
         //retrieve the command list arguments
      String girlNameFile = args[0];
      
         //call read Data method to populate girlNameList   
       readData( girlNameList, girlNameFile );     

       System.out.print("Enter a girls name to search: ");
       String name = console.next();
       
         //call search method
       int foundIndex = search(girlNameList, name);
       
       if(foundIndex == -1) {
         System.out.println("Not found");
       }
       else {
         System.out.println("Found at index " + foundIndex );
       }       
       
      
   }//end main
   
   //readdata method
   private static void readData(ArrayList list, String fileName) throws IOException{
      
     Scanner inFile = new Scanner( new File(fileName) );
      
      while( inFile.hasNext() ) {
         
         //read a name and place it into the array list
         list.add(inFile.next());

      }

      inFile.close();

   }
   
      //serach method
   private static int search(ArrayList list, String name) {
   
      for(int i=0; i<list.size(); i++) {
         if( list.get(i).toString().equalsIgnoreCase(name) ) {
            return i;
         }

      }
      
      return -1; //no tfound
      
   }
   
}//end class