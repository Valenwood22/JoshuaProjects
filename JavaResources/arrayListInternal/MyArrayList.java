public class MyArrayList<E> implements ArrayListInterface<E> {

     //data members
   private E[] a;  //a generic array
   private int capacity = 16;
   private int size = 0;  //number of ojects
    
      //constructor
   public MyArrayList() {
      a = (E[]) new Object[capacity];
   }
    
   public int size() {
      return size;
   }
    
   public boolean isEmpty() {
      return size == 0;
   }
    
   public E get(int i) throws IndexOutOfBoundsException {
    
       //check to see if i is out of bound
      checkIndex(i, size);
     
      return a[i];
   }
    
   public E set(int i, E obj) throws IndexOutOfBoundsException {
    
       //check to see if i is out of bound
      checkIndex(i, size); 
       
      E temp = a[i]; //retrieve the current object
      a[i] = obj;    //replace it with the new object
   
      return temp;
   }
    
   public E remove( int i ) throws IndexOutOfBoundsException {
   
       //check to see if i is out of bound
      checkIndex(i, size); 
      
      E temp = a[i];  //retrieve the removed object
       
       //use a loop from i to size - 1
      for( int x = i; x < size - 1; x++ ) {
         a[x] = a[x+1];
      }
       
      size--;
       
      return temp;
   
   } //end remove method
    
   public void add( int i, E obj ) throws IndexOutOfBoundsException {
    
            //check to see if i is out of bound
      checkIndex(i, size + 1);    
            
            //check the capacity
            //if the array is full, extent it
            
      if(size == capacity) {  //array is full
      
           capacity = capacity * 2; //double the capacity
           E[] b = (E[]) new Object[capacity]; //create a new array 
           
           for( int x=0; x<size; x++) {
               b[x] = a[x];  //copy the elements from a to b
           }
      
           a = b; //rename b to a
      
      }     
           
            //shift objects to make room for the new object
      for(int x = size-1; x >= i; x--) {
         a[x+1] = a[x];
            
      }
            
      a[i] = obj;
            
      size ++;
    
   } //end add method
      
   private void checkIndex( int i, int n ) throws IndexOutOfBoundsException {
   
      if( i >= n || i < 0 ) {
         throw new IndexOutOfBoundsException("Illegal index: " + i );
      }
      
      //if no exception, then i is inbound
   
   }
   
   public String toString() {
   
      String result = "[ ";
       
      for(int x = 0; x < size; x++) {
       
         result += " " + a[x];
       
      }
       
      return result + " ]";
   } 
 
} //end class























