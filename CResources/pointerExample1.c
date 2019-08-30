/*  Name: Joshua Gisi
	ECE 173 Lab assignment #8
    Due date: November 29, 2018 at 5 PM */
   
#include <stdio.h>

//declare methods used
void printArray(int* array, int length);
void sort(int* array, int length);

//Main Method
int main()
{
    //declare varaiables
	int arrayLength=0;
	int input;
	int i;
	
	//ask the user how long the array should be?
	printf("How many Integers would you like to enter into an array? ");
	scanf("%d",&arrayLength);
	int array[arrayLength];
	
	//Ask the user to fill the array with integers
	for(i=0; i<arrayLength; i++ ){
		printf("Enter an integer at position %i: ", i+1);
		scanf("%d",&input);
		array[i]=input;
	}

	//prints the array elemnts that where just entered
    printf("\n\nElements before sorting: ");
    printArray(array, arrayLength);

	//prints the array elements after being sorted 
    printf("\n\nArray after sorting (using pointers): ");
    sort(array, arrayLength);
    printArray(array, arrayLength);

	//The main method is expecting an integer return
    return 0;
}


//A simple method to print each of the elements in an array seperated by a comma
void printArray(int* array, int length)
{
	int i;
	for(i=0; i<length; i++){
		printf("%d, ", *(array++));
	}
	
}

//A method to sort an a array using pointers.
//Because it uses pointers it can be a void method
void sort(int *array, int length){
	//declare flow control varaiables
    int *i, *j, temp;
    
	//a bubble sort is 2 nested for loops which completes the sorting in 
	//O(N^2) time. This is not as fast as a quick sort ie. O(Nlog(N)) but
	//it does the job for this assignment
    for(i = array; i < array + length; i++){
        for(j = i + 1; j < array + length; j++){
        	//if the sorting runs into an integer that is out of order
			//it swaps the integers position using pointers
            if(*j < *i){
                temp = *j;
                *j = *i;
                *i = temp;
            }
        }
    }
}

