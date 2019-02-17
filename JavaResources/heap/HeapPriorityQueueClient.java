import java.util.Scanner;

public class HeapPriorityQueueClient {

    static final Scanner console = new Scanner(System.in);
    
    public static void main(String[] args) {
      HeapPriorityQueue<Integer> pq1 = new HeapPriorityQueue<Integer>();
      
      pq1.enqueue( 8 );
      pq1.enqueue( 18 );
      pq1.enqueue( 3 );
      pq1.enqueue( 13 );
      pq1.enqueue( 29 );
      pq1.enqueue( 19 );
      pq1.enqueue( 2 );
      pq1.enqueue( 7 );
      
      System.out.println( "\n" + pq1.toString() + "\n" );
      
      System.out.println( pq1.dequeue() + " is removed\n" ); 
      
      System.out.println( "\n" + pq1.toString() + "\n" );  

    }
}
