/*
 *
 *
 *
 * This queue can never hold more than n - 1 objects
 */

public class MyArrayQueue<E> implements QueueInterface<E> {

   public static final int CAPACITY = 10;
   
   private int capacity;
   
   private E[] myQueue;
   
   private int front;
   
   private int rear;
   
   //constructor
   public MyArrayQueue() {
      this(CAPACITY);
   }
   
   //overloaded constructor
   public MyArrayQueue(int n) {
      capacity = n;
      myQueue = (E[]) new Object[capacity];
      front = 0;
      rear = 0;
   }
   
   public boolean isEmpty() {
      return (front == rear);
   }
   
   public E peek() throws EmptyQueueException {
      
      if( isEmpty() ) {
         throw new EmptyQueueException("Empty Queue");
      }
      
      return myQueue[front];
      
   }
   
   public void enqueue( E obj ) throws FullQueueException {
      
      if( size() == capacity - 1) { //cannot hole more than n-1 objects
         throw new FullQueueException("Queue Overflow");
      }
      
      myQueue[rear] = obj;
      
      rear = (rear + 1) % capacity; //need to wrap it around
      
   }
   
   public E dequeue() throws EmptyQueueException {
      if( isEmpty() ){
         throw new EmptyQueueException("Empty Queue");
      }
      
      E temp = myQueue[front];
      
      myQueue[front] = null;
      
      front = front + 1; //need to circulate front
      
      return temp; 
      
   }
   
   public int size() {
      return (capacity - front + rear) % capacity;
   }
   
   public String toString() {
      
      return "";
   }   
}