/*
 *
 *
 *
 */
 
import java.util.*;

@SuppressWarnings("unchecked")

public class HeapPriorityQueue< E extends Comparable<E> > implements QueueInterface<E> {
   
   //data members
   private ArrayList<E> priorityQ;
   private int lastIndex;
   
   //constructor
   public HeapPriorityQueue() {
      priorityQ = new ArrayList();
      lastIndex = 0;
   }
    
   public int size() {
      return lastIndex;
   }
   
   public boolean isEmpty() {
      return lastIndex == 0;
   }
   
   public E peek() throws EmptyQueueException {
   
      if( isEmpty() ) {
         throw new EmptyQueueException("Empty Queue" );
      }
      return (E) priorityQ.get(0); //retrun the object at the root
   }
   
   public void enqueue( E newObject ) {
   
      priorityQ.add( lastIndex, newObject );
      
      if(lastIndex == 0) {
         lastIndex ++;
         return;
      }
      
      //up-heap building 
      int parentIndex;
      int currentIndex = lastIndex;
      
      while(true) {
         
         //determine if the newObject is a left or right child
         if(currentIndex %2 ==1) { //left child
            parentIndex = (currentIndex - 1)/2;
         }         
         else { //right child
            parentIndex = currentIndex / 2-1;
         }
              
         //compare the newObject with its parent
         E child = priorityQ.get(currentIndex);
         E parent = priorityQ.get(parentIndex);
         
         if( child.compareTo(parent) < 0) { //child < parent so swap
            //swap them
            E temp = (E) priorityQ.get(currentIndex);
            priorityQ.set( currentIndex, priorityQ.get(parentIndex));
            priorityQ.set(parentIndex, temp);
         }
         
         //continue the proces sto the root
         currentIndex = parentIndex;
         
         if(currentIndex == 0) {
            break;
         }
      }//end while
      
      lastIndex++;
      
   }//end enqueue
   
   public E dequeue() throws EmptyQueueException {
   
      if(isEmpty() ) {
         throw new EmptyQueueException("Empty Queue");
      }
      
      E removedObj = (E) priorityQ.get(0); //retreve the object at root
   
      if( lastIndex == 1 ){   //only one node in the heap
         priorityQ.set(0, null);
         lastIndex --;
         return removedObj;
      }
      
      if( lastIndex == 2 ) {   //only one node remaining
         priorityQ.set(0, priorityQ.get(lastIndex -1) );
         priorityQ.set(lastIndex - 1, null);
         lastIndex--;
         return removedObj;
      }
      
         //The heap has more than 2 nodes
      
         //make the last node as the new root
      priorityQ.set(0, priorityQ.get(lastIndex-1));
      priorityQ.set(lastIndex-1, null);
      lastIndex--;
      
      int parentIndex=0;
      int currentIndex=0;
      
      while(true) {
         
         //find the index of teh two childern
         int leftChildIndex = 2 * currentIndex + 1;
         int rightChildIndex = 2 * (currentIndex + 1);
         
         int minChildIndex;
         
         if(leftChildIndex >= lastIndex && rightChildIndex >= lastIndex ) { //no Childern
            break;
         }
         else if( rightChildIndex >= lastIndex ) { //no right child, only left child
            minChildIndex = leftChildIndex;
         }
         else { //two childern
         
            //find the smaller child
            E left = priorityQ.get(leftChildIndex);
            E right = priorityQ.get(rightChildIndex);
            
            if(left.compareTo(right) < 0) {
               minChildIndex = leftChildIndex;
            }
            else {
               minChildIndex = rightChildIndex;
            }
         }
            //compare the parent with the smaller child
         if( priorityQ.get(minChildIndex).compareTo(priorityQ.get(currentIndex)) < 0 ) {
            //swap them
            E temp = (E) priorityQ.get(currentIndex);
            priorityQ.set(currentIndex, priorityQ.get(minChildIndex));
            priorityQ.set(minChildIndex, temp);
         }   
         
         currentIndex = minChildIndex;
         
      }//end while
      
      priorityQ.remove( null );
      
      return removedObj;
      
   }//end dequeue
   
   public String toString() {
      return "" + priorityQ;
   }
   
   
}//end class