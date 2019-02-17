
   //This linked list works for the generic comaprable objects
   
public class MyLinkedList<E extends Comparable<E> > {
	
	//data members
   private Node<E> head;
   private Node<E> tail; //your homework!!
   private int size;

   //constructor
   public MyLinkedList() {
      head = null;
      //do something with tail....homework.
      size = 0;
   }

   //size method
   public int size(){
      return size;
   }

   //isEmpty method
   public boolean isEmpty(){
      if(head == null){
         return true;
      }
   
      return false;
   }

   //addFirst method will add a new node as the first node
   public void addFirst( E element ){
      //step 1: create a new Node for the element
      Node<E> temp = new Node<E>( element, null );
   
      //you need to do something with the tail in the homework.
   
      if(isEmpty()) {
         head = temp;
      }
      else{
         //step 2: temp.next = head
         temp.setNext(head);
         head = temp; //step 3
      }
      size++; //step 4
   }
   
   //removeFirst method will remove and return the first node
   public E removeFirst() throws EmptyListException {
   
      if( isEmpty() ) {
         throw new EmptyListException("The linked list is empty.");
      }
   
      Node<E> temp=head; //step 1
      
      //if the list has one node, do something with the tail reference
      
      head=head.getNext();//step 2
   
      temp.setNext(null); // temp.next = null
   
      E result=temp.getElement(); //step 4 retrieve the object      
   
      size--;
   
      temp = null;
   
      return result; 
   
   }

      //add the new node as th elast node
   public void addLast( E element )  {
      //this is the homework
      //use the tail efernce to add the new node
      //do not traverse the list
      
   }
   
      //traverse the list
   public String traverse() {
      
      if( isEmpty() ) {
         return "Empty List";
      }
      
      Node<E> temp=head;
      
      String result = "head --->";
      
      int i=size;
      
      while( i>0  ) {
         
         result += temp.getElement() + "--->";
         temp = temp.getNext();
         i--;
         
      } 
      
      return result;
   }
   
      //sort the list usin ghte selection sort
   public void selectionSort() {
   
      Node<E> minNode, tempHead, tempHeadNext;
      
      tempHead = head;
      tempHeadNext = head.getNext();
   
      for(int x=0; x<size-1; x++) {
      
         minNode=tempHead;
      
         for(int i=x+1; i<size; i++) {
            if( (tempHeadNext.getElement()).compareTo(minNode.getElement()) < 0 ) {
               minNode = tempHeadNext;
            }
            
            tempHeadNext = tempHeadNext.getNext();//move to the next node
         }
      
         //swap
         E temp = tempHead.getElement();
         tempHead.setElement( minNode.getElement() );
         minNode.setElement( temp );
      
         tempHead = tempHead.getNext();
         tempHeadNext = tempHead.getNext();
      }
      
   }
   
      //search an elemnt in the linked list
      //return true if found  
   public boolean search( E searched ) {
      //this is homework
      
      //it searches the entire list, return tre if found
      
      
      // go over the entire list simular to traverse // use if( temp.getElement.compareTo(serched) == 0 )
      return false;
    
    
   }
   
      //add a new node as the second nde
   public void addSecond( E element ) {
   
      //cretet a new node for the element
      Node<E> temp = new Node<E>(element, null);
      
      if( isEmpty() ) {
         System.out.println("The list is empty");
         
      }
      else {
         
            //temp's next = head.next
         temp.setNext( head.getNext() );
         
            //heads next =  temp
         head.setNext( temp );
         
         temp =null;
         
         size++;
                     
      }
      
   }
   
      //remove the second node and return the element object
   public E removeSecond() throws Exception {
      
      if( size<2 ) {
         
         throw new Exception("The list has less than two nodes.");    
      }
      
      Node<E> temp = head.getNext();
      
         //heads nest = temps next
      head.setNext( temp.getNext() );
      
         //temo next to null
         temp.setNext(null);

         size--;

         E element = temp.getElement();

         temp=null;

         return element;
                   
      }
      
}//end of class