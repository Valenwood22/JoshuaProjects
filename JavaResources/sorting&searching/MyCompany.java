
import java.io.*;
import java.util.*;

public class MyCompany
{
    public static void main(String[] args) throws FileNotFoundException
    {
        EmployeeInfo[] all = new EmployeeInfo[11];

        Scanner inFile =
		              new Scanner(new FileReader("employee_data.txt"));

		  for (int i = 0; i < all.length; i++) {
		      all[i] = new EmployeeInfo();
        }
    
	     int id;    
		  String fName, lName;
        double salary;
    
		  for (int i = 0; i < all.length; i++)
        {
			   id = inFile.nextInt();  
				fName = inFile.next();
			   lName = inFile.next();

            salary = inFile.nextDouble();

            all[i].setId(id); 
				all[i].setFirstName(fName);
            all[i].setLastName(lName);
            all[i].setSalary(salary);
		  }

      boolean flag = true;
		int userCommand;
		Scanner console = new Scanner(System.in);

		
      while(flag) {
		
		    displayMenu();
			           
			 userCommand = console.nextInt();
          
			 switch(userCommand) {
    	       case 1:
                 System.out.println("\nId     First_Name   Last_Name    "
                          + "Salary");

		           for (int i = 0; i < all.length; i++) {
		              System.out.println(all[i]);
                 }
					  
					  break;
					  				
				 case 2:   
					  //call quick sort method
                  QuickSortProgramComparable.quickSort( all, 0, all.length-1);
                  
                  System.out.println("The array is sorted.");  
                  
				     break;

             case 3:  
					  
					  
					  
				     break;

				 case 0:
				     flag = false;
					  break;
				
				 default:
				     System.out.println("Invalid command, try again.");
					  
          }//end of switch
	     }//end of while
		  
		  System.out.println("\n\nThank you for using this program");
	 
	 }//end main
	 
	 private static void displayMenu() {
	      System.out.print("\n\n"
			       +"1 --- Output the employee informaiton\n"
		          +"2 --- Quick sort\n"
					 +"3 --- Binary search\n"
					 +"0 --- Exit\n\n"
		          +"Enter a command: " ); 
	 } //end displayMenu
	 
		 
} //end class