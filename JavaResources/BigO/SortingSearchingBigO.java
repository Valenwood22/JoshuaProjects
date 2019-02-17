import java.util.*;                                       

public class SortingSearchingBigO
{                                                        
   static Scanner console = new Scanner(System.in);      

   public static void main(String[] args)                
   {                                                     
      int k;
        		
      int [] list = null;;
      
      long before, after;
   		   		
      boolean flag = true;
   		
      while( flag ) {
      
         System.out.println();
         System.out.println("******************");
         System.out.println("1 --- Prompt the user to enter the size of array\n" +
                                   "      Create an array based on the user input\n" +
                                   "      Populate the array with random numbers");
         System.out.println("2 --- Call Selection Sort method and record the running time");
         System.out.println("3 --- Call Bubble Sort method and record the running time");
         System.out.println("4 --- Call Insertion Sort method and record the running time");
      
         System.out.println("5 --- Call Quick Sort method and record the running time");
         System.out.println("6 --- Call Sequential Search method and record the running time");
            
         System.out.println("7 --- Call Binary Search method (non-recursive) and record the running time");
         System.out.println("8 --- Call Binary Search method (recursive) and record the running time");
      
         System.out.println("0 --- Exit");
         System.out.println("*******************");
           
         System.out.print("\nEnter your selection: ");
         k = console.nextInt();
            
         switch(k) {
            case 1:
            
               System.out.print("Enter the size of array: ");
               int n = console.nextInt();
            
               list = new int[n];
               Random rand = new Random();
            
               for(int i=0; i<list.length; i++) {
                  list[i] = rand.nextInt();
               }
            
               System.out.println("\n" + n + " random numbers were generated and placed in the array.");
                          
               break;
         			  
            case 2:
                  
               before = System.currentTimeMillis();

               IntSelectionSorter.selectionSort( list );
               
               after = System.currentTimeMillis();
               
               System.out.println("\nSelection Sort Time: " + (after-before) + " milliseconds.");
            	                              
               break;
         			  
            case 3:
                    
            		  
            		                      
               break;
         			  
            case 4:
                   
            		 
               break;
               
            case 5:
            
               before = System.currentTimeMillis();
               
               IntQuickSorter.quickSort( list );
               
               after = System.currentTimeMillis();
               
               System.out.println("\nQuick Sort Time: " + (after-before) + " milliseconds.");                          
            		  
            		                      
               break;
         			  
            case 6:
                   
            		 
               break;
         
            case 7:
                    
            		  
            		                      
               break;
         			  
            case 8:
                   
            		 
               break;
         
         			  
            case 0:
            	 
               flag = false;
            		  
               break;
         			  
            default:
               System.out.println("Invalid, try again");
         			  
         }//end switch
      }//end while
   
   						  
   }//end main             
	 
	                                               
                                       
}//end class