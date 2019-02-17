``
public class MyLinkedListClient {

	public static void main(String [] args) {
	
      //create a linked list of string
      MyLinkedList<String> airportList = new MyLinkedList<String>();
      
      //addFirst
      airportList.addFirst("ALT");
      airportList.addFirst("BOS");
      airportList.addFirst("STL");
      airportList.addFirst("MSP");
      airportList.addFirst("RST");   
		
      //traverse the list
		System.out.println( airportList.traverse() );
		
      //selecton sort
      airportList.selectionSort();
      
      //travers the list
      System.out.println( airportList.traverse() );
      
      
      //remove First
      System.out.println( airportList.removeFirst() + " is removed");
      System.out.println( airportList.removeFirst() + " is removed");
      
      //traverse the list
		System.out.println( airportList.traverse() );
      
		
      
	} //end main

}//end of class