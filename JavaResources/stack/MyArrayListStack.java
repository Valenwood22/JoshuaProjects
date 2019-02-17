import java.util.*;

@SuppressWarnings("unchecked")

public class MyArrayListStack<E> implements StackInterface<E> {

   private ArrayList<E> s;
   public static final int CAPACITY=12;
   
   private int capacity;
   
   private int top;
   
      //defalt constructoe
   public MyArrayListStack() {
      this(CAPACITY);
   }
      //overloaded constructor
   public MyArrayListStack( int n ) {
      capacity=n;
      s=new ArrayList<E>(capacity);
      
      top=-1;
   
   }         
   
      //size method 
   public int size() {
      return top+1;
      
   }    
   
   //isEmpty method
   public boolean isEmpty() {
      if(top == -1) {
         return true;
      }
      return false;
   }
   
      //push method
   public void push( E element ){
      top++;
      s.add(top, element);
   }   
  
      //peek
   public E peek() throws EmptyStackException {
      if( isEmpty() ) {
         throw new EmptyStackException("Empty Stack");
      }
      
      return s.get(top);
   } 
   
      //pop
   public E pop() throws EmptyStackException {
      if( isEmpty() ) {
         throw new EmptyStackException("Empty Stack");
      }
      
      E temp = s.remove(top);
      
      top--;
      
      return temp;
   }       
   
   public String toString() {
      String results = "";
      
      for(int i=top; i>=0; i--) {
         results += s.get(i) + "\n";
      }
      return results;
   }
     
}//end of class













