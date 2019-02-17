public interface ArrayListInterface<E> { 

     public int size();

     public boolean isEmpty();

     public E get(int i) throws IndexOutOfBoundsException;

     public E set(int i, E e) throws IndexOutOfBoundsException;

     public void add(int i, E e) throws IndexOutOfBoundsException;

     public E remove(int i) throws IndexOutOfBoundsException; 

}