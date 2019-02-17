
import java.util.ArrayList;

public class MyArrayListQueue<E> implements QueueInterface<E> {

   private ArrayList<E> q;
   private int front;
   private int rear;
   
   private int capacity;
   
   public static final int CAPACITY = 10; //default
   
      //default constructor
   public MyArrayListQueue() {
      this(CAPACITY);
   }     
     
     //overloadd constructor
   public MyArrayListQueue( int n ) {
      capacity = n;
      
      q = new ArrayList<E>();
      
      front = rear = 0;
   }
   
   public boolean isEmpty() {
      return (front == rear);   
   }
   
   public int size() {
      return q.size();
   }
   
   public void enqueue( E obj ) {
      
      q.add(rear, obj);
      
      rear++;  
   }   
   
   public E peek() throws EmptyQueueException {
      
      if( isEmpty() ) {
         throw new EmptyQueueException("Empty Queue");
      
      }
      
      return q.get(front);
   }
   
   public E dequeue() throws EmptyQueueException {
      
      if( isEmpty() ) {
         throw new EmptyQueueException("Empty Queue");
      }
      
      rear--;
      
      return q.remove(front);
   }
   
   public String toString() {
      return "" + q;   
   }
   
}//end class