/*  Name: Joshua Gisi
	ECE 173 Lab assignment #5
    Due date: October 18, 2018 at 5 PM */
    
#include <stdio.h>

//declare structure
struct product{
	int id;
	float price;
};
struct product productList[5];	

//declare methods
void getInput();
void displayProductList();
void sortProductList();

int main (void) {
	
	getInput();
	printf("\nBefore sorting\n");
	displayProductList();
	printf("\nAfter sorting\n");
	//sortProductList();
	
	
			
	return 0;
}

//A method to find the mean 
void getInput(){
	
	//declare local flow control varaiables
	int i, id;
	float price;
		
	//get user input
	for(i=1; i<6; i++) {
		printf("\nEnter data for record #%i", i );
		printf("\nEnter ID: ");
		scanf("%i",&id);
		printf("Enter price: ");
		scanf("%f",&price);
		productList[i-1].id=id;
		productList[i-1].price=price;			
	}		
	
}

//print array emelnets
void displayProductList(){
	int i;
	printf("\nID          Price");
	for(i=0; i<5; i++){
		printf("\n%i          $%.2f",productList[i].id, productList[i].price);
	}
}

//bubble sort array
void sortProductList(){
	do
	{
    	switched = false;
    	for(i = 1; i < 5; i++)
    	{
        	if(myFloatArr[myFloatIndex[i - 1]] < myFloatArr[myFloatIndex[i]])
        	{
    	        int temp = myFloatIndex[i];
	            myFloatIndex[i] = myFloatIndex[i - 1];
            	myFloatIndex[i - 1] = temp;
        	    switched = true;
    	    }
	    }
	}
	while(switched);
	
	displayProductList();
}





