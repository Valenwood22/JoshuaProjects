import java.util.*;                                       

public class PrefixAverages
{                                                        
    static Scanner console = new Scanner(System.in);      

    public static void main(String[] args)                
    {                                                     
         int n, k;
			System.out.print("Enter the size of array: ");
			n = console.nextInt();
			
			long before, after;
			
			int [] list = new int[n];
			
			for(int i=0; i<list.length; i++) {
			     list[i] = (int)(Math.random() * 100 +1);
			}
			
			System.out.println("\n" + n + " random numbers were generated in an array.");

			
			boolean flag = true;
			
		   while( flag ) {
			   System.out.println();
				System.out.println("******************");
            System.out.println("1 - Big O(n)");
            System.out.println("2 - Big O(n^2)");
            System.out.println("3 - Big O(n^3)");
            System.out.println("4 - Big O(2^n)");
				System.out.println("5 - Big O(log n)");
            System.out.println("6 - Big O(n * long n)");
            System.out.println("0 - Exit");
				System.out.println("*******************");

            System.out.print("\nEnter your selection: ");
            k = console.nextInt();
            
            switch(k) {
                case 1:
										 
                    before = System.currentTimeMillis();
						  
						  
						  
						 						  
						  after = System.currentTimeMillis();
			
			           System.out.println("\nTime spent: " + (after-before) + " milliseconds");
                         
                    break;
						  
                case 2:
					     
						 
						           
                    break;
						  
                case 3:
                    
						  
						                      
                    break;
						  
                case 4:
                   
						 
						  break;
						  
                case 0:
					 
                    flag = false;
						  
                    break;
						  
                default:
                    System.out.println("Invalid, try again");
						  
            }//end switch
        }//end while

							  
    }//end main             
	 
	   //linear method
    public static void linearMethod( int [] list) {
	     
		  
	 }         
	 
	   //quadric method
	 public static void quadricMethod( int [] list) {
	     
	 
	 }   
	 
	  //cubic method
	 public static void cubicMethod( int [] list) {
	     
	 }   
	 
	  //logN method
	 public static void logNMethod( int [] list) {
	     
    }   
	 
	  //NlogN method
	 public static void nLogNMethod( int [] list) {
	     
	 }   
	 
	  //exponential method
	 public static void exponentialMethod( int [] list) {
	     
	 }                                                                                                    
                                       
}//end class
