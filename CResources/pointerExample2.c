/*  Name: Joshua Gisi
	ECE 173 Lab assignment #8
    Due date: November 29, 2018 at 5 PM */
    
#include <stdio.h>

//Main Method
int main (void) {
	
	//Declare varaiables and pointers
	int integer;
	int *ptrInt;
	float floating;
	float *ptrFloat;
	char character;
	char *ptrChar;
	
	//Ask for an integer user input and store the pointer 
	printf("Please, enter a whole number (without a decimal point): ");
	scanf("%i", &integer);
	ptrInt = &integer;
	
	//Ask for a floating user input and store the pointer 
	printf("Please, enter a decimal number: ");
	scanf("%f", &floating);
	ptrFloat = &floating;
	
	//Ask for the unser to input a chararrcter and store the pointer 
	printf("Please, enter any keyboard character: ");
	scanf(" %c", &character);
	ptrChar = &character;

	//print the entered Integer and its address
	printf("\nThe whole number entered is %i.", integer);
	printf("\nThe address of the %i is %p", *ptrInt, ptrInt);
	
	//print the entered float and its address
	printf("\n\nThe decimal number entered is %f.", floating);
	printf("\nThe address of the %f is %p", *ptrFloat, ptrFloat);
	
	//print the enteres character and its address
	printf("\n\nThe character entered is %c.", character);
	printf("\nThe address of the %c is %p", *ptrChar, ptrChar);
	
	printf("\n======================================");
	
	//ask for a new interger and modify the existing integer via pointers
	printf("\nThe new value of the whole number you entered was modified by adding 100.");
	integer = *ptrInt + 100;
	printf("\nIts value is now: %i", integer);
	printf("\nIts address is: %p", &integer);
	
	//ask for a new float and modify the existing float via pointers
	printf("\n\nThe new value of the decimal number you entered was modified by subtracting 50.");
	floating = *ptrFloat - 50;
	printf("\nIts value is now: %i", integer);
	printf("\nIts address is: %p", &integer);
	
	//ask for a new character and modify the existing character via pointers
	printf("\n\nPlease, enter a new keyboard character: ");	
	scanf(" %c", &character);
	
	printf("\nThe new character you entered is: %c", character);
	printf("\nIts address is: %p", &character);
			
	//We must use the 'return 0' since we declared the main method as an 'int main()'
	//and not a 'void main()'. Because it's an 'int main()' method, the compiler is 
	//expecting an integer return even though it has no use.
	return 0;
}








