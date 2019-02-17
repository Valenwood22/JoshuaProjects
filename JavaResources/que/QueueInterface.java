
public interface QueueInterface<E> {

  public int size();

  public boolean isEmpty();

  public E peek() throws EmptyQueueException;

  public void enqueue (E element);

  public E dequeue() throws EmptyQueueException;
}