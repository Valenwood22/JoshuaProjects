public class MyArrayListClient {
   
   public static void main(String[] args) {
   
       //create a MyArrayList object
       
      MyArrayList<Integer> aList = new MyArrayList<Integer>();
       
      aList.add(0, 7);
      aList.add(0, 4);
      aList.add(2, 12);
      aList.add(1, 9);
       
      System.out.println( aList );
       
      System.out.println( aList.get(2) + " is returned." );
       
      System.out.println( aList.remove(1) + " is removed." );
       
      aList.set(0, 100);
   
      System.out.println( aList );
   
   }
}























