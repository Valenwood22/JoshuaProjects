
public class MyArrayQueueClient {

   public static void main(String[] args) {
   
      MyArrayListQueue<String> customerQ = new MyArrayListQueue<String>();
     
      customerQ.enqueue("Tom");
      customerQ.enqueue("Ben");
      customerQ.enqueue("Mary");
      customerQ.enqueue("John");
      
      System.out.println("\nQueue: " + customerQ);
      
      System.out.println("\nServing Customer: " + customerQ.dequeue() );
      System.out.println("\nServing Customer: " + customerQ.dequeue() );
      
      System.out.println("\nQueue: " + customerQ );
   	
   } //end main
	
}//end class
