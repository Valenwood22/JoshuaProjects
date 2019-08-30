/*  Name: Joshua Gisi
	ECE 173 Lab assignment #5
    Due date: October 18, 2018 at 5 PM */
    
#include <stdio.h>

int main (void)
{

	//declare flow control varaiables
	int array[]={ 34, -5, 6, 0,12,100,56,22,44,-3,-9,12,17,22,6,11 };
	int i;
	char input;
	
	printf("Hello, press 'D' to print the array in descending order or 'A' to print the array in ascending order: ");
	scanf("%d",&input);
	
	switch(input);
		case 'A':
			break;
		case 'D':
			break;
		default
			printf("Enter 'D' for descending and 'A' for Ascending");
	
	
	//Print results from methods 
	sort(array, 16);
	
	for(i=0; i<16; ++i){
		printf("%i, ", array[i]);
	}
			
	return 0;
}

//A method to find the mean 
void sort(int a[], int n){
	int i, j, temp;
	
	for(i=0; i<n-1; ++i){
		for(j=i+1; j<n; ++j) {
			if(a[i] > a[j] ){
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}	
	}
	
}

