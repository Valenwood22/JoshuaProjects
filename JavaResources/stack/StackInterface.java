/*
 
 */
 
public interface StackInterface<E> {

   public int size();
   
   public boolean isEmpty();
   
   public void push( E element );
   
   public E pop() throws EmptyStackException;
   
   public E peek() throws EmptyStackException;
    
 
}