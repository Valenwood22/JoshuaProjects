/**
   The RecursiveBinarySearcher class provides a public static
   method for performing a recursive binary search on an int array.
*/

public class RecursiveBinarySearcher
{
   /**
      The search method calls the doBinarySearch method
      to search for a value in an array.
      @param array The array to search.
      @param value The value to search for.
   */
   
   public static int search(int[] array, int value)
   {
      return binarySearch(array, 0, array.length - 1, value);
   }
   
   /**
      The binarySearch method performs a recursive binary
      search on an integer array. 
      @param array The array to search.
      @param first The first element in the search range.
      @param last The last element in the search range.
      @param value The value to search for.
      @return The subscript of the value if found,
              otherwise -1.
   */

   private static int binarySearch(int[] array, int first,
                                     int last, int value)
   {
      int middle;     // Mid point of search
        
      // Test for the base case where the
      // value is not found.
      if (first > last)
         return -1;
        
      // Calculate the middle position.
      middle = (first + last) / 2;
       
      // Search for the value.
      if (array[middle] == value)
         return middle;
      else if (array[middle] < value)
         return binarySearch(array, middle + 1,
                             last, value);
      else
         return binarySearch(array, first,
                             middle - 1, value);
   }

}