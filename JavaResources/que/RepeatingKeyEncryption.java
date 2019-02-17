/*
* Author: Joshua Gisi
* Date: 4/11/18
*/

import java.util.*;
public class RepeatingKeyEncryption {

   public static void main(String[] args) {
   
      //declar evaraibles
      String message = "Knowledge is power.";
      int [] key = {6,7,3,1,8};
      
        //call encrypt
      System.out.println("\nEncrypted message: " + encrypt(message, key) );  
      
         	
   } //end main
	
   
   
      //encryption method
   public static String encrypt( String message, int [] key) {
      
      String encoded = "";
      int keyValue;
      
      //create a Queue
      Queue<Integer> keyQueue = new LinkedList<Integer>();
      
      //load the key values to keyQueue
      for(int i=0; i<key.length; i++) {
         keyQueue.add( key[i] ); //enqueue
      }   
      
      //encrypt the message
      for(int i=0; i<message.length(); i++) {
         keyValue = keyQueue.remove();
         encoded += (char) (message.charAt(i) + keyValue);
         keyQueue.add( keyValue); //enqueue       
      
      }
      
      return encoded;
   
   }   
}//end class