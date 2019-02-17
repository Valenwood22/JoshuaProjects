/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lt2025vt
 */
import java.io.*;
import java.util.*;
import javax.swing.JFileChooser;

public class HardwareStoreClient {

    static final int SIZE = 15;

    public static void main(String[] args) throws IOException {

        //create an array of Inventory 
        Invenory[] itemList = new Invenory[SIZE];

        String inputFileName;

        while (true) {
            JFileChooser open = new JFileChooser("./");

            int status = open.showOpenDialog(null);

            if (status == JFileChooser.APPROVE_OPTION) {
                //open button is a clicked
                inputFileName = open.getSelectedFile().getAbsolutePath();
                break;
            }
        }//end while

        //read data from the data file
        Scanner inFile = new Scanner(new FileReader(inputFileName));

        //remove the data file headings 
        for (int i = 0; i < 4; i++) {
            inFile.next();
        }

        int pid;
        String pName;
        int pieces;
        double unitPrice;

        int x = 0;
        //read data, create objects, and populate the array
        while (inFile.hasNext()) {
            pid = inFile.nextInt();
            pName = inFile.next();
            pieces = inFile.nextInt();
            unitPrice = inFile.nextDouble();

            //create an instant (object) of Inventory
            itemList[x] = new Invenory(pid, pName, pieces, unitPrice);
            x++;
        }

        boolean flag = true;
        int userCommand;
        Scanner console = new Scanner(System.in);

        while (flag) {
            showMenu();

            userCommand = console.nextInt();

            switch (userCommand) {
                case 1:
                    for (int i = 0; i < itemList.length; i++) {
                        System.out.println(itemList[i]);
                    }
                    break;
                case 2:
                    double sum = 0.0;
                    for (int i = 0; i < itemList.length; i++) {
                        sum += itemList[i].calculateInStockValue();
                    }

                    System.out.printf("%nTotal In-Stock Value: $ %.2f %n", sum);
                    break;
                case 3:
                    int maxIndex = 0;

                    for (int i = 0; i < itemList.length; i++) {
                        if (itemList[maxIndex].calculateInStockValue()
                                < itemList[i].calculateInStockValue()) {

                            maxIndex = i;
                        }
                    }

                    System.out.println("\nThe Highest In-Stock Value Item:\n");
                    System.out.println(itemList[maxIndex]);

                    break;
                case 4:
                    System.out.println("Low In-Stock Items: \n");

                    for (int i = 0; i < itemList.length; i++) {
                        if (itemList[i].getNumberOfPrices() < 10) {
                            System.out.println(itemList[i]);
                        }
                    }
                    break;
                case 5:
                    System.out.println("\nenter a product to search");

                    String searched = console.next();

                    int foundIndex = search(itemList, searched);

                    if (foundIndex == -1) {
                        System.out.println(searched + " is not found.");
                    } else {
                        System.out.println(itemList[foundIndex]);
                    }

                    break;
                case 6:
                    //selection sort
                    selectionSortByName(itemList);
                    System.out.println("The item list is sorted.");

                    break;
                case 7:
                    selectionSortByName(itemList);
                    //binary search
                    System.out.print("Enter an item name to search: ");
                    String key = console.next();
                    foundIndex = binarySearchRecursion(itemList, 0, itemList.length - 1, key);

                    if (foundIndex == -1) {
                        System.out.println(key + "is not found.");
                    } else {
                        System.out.println("Found at index " + foundIndex);
                        System.out.println(itemList[foundIndex]);
                    }

                    break;
                case 8:
                    //quick sort
                    quickSort( itemList, 0 , itemList.length -1);
                    
                    System.out.println("The array is sorted.");
                    
                    break;
                case 0:
                    flag = false;

                    break;
                default:
                    System.out.println("Invalid command, try again");
            }//end switch
        }//end While
    }//end main

    //print a user menu
    private static void showMenu() {
        System.out.print("\n\n"
                + "1 - Output the inventory\n"
                + "2 - Output the total inventory\n"
                + "3 - Find the items with the highest in-Stock value\n"
                + "4 - Find the low in-stock items\n"
                + "5 - Search an item\n"
                + "6 - Selection sort by item name\n"
                + "7 - Search an item using binary search algorithm\n"
                + "8 - Quick sort by item name\n"
                + "0 - Exit\n\n"
                + "Enter a command: ");

    }//end show menue

    //search method
    private static int search(Invenory[] itemList, String searched) {

        for (int i = 0; i < itemList.length; i++) {
            if (itemList[i].getItemName().equalsIgnoreCase(searched)) {
                return i;
            }
        }

        return -1;
    }

    //selection sort method
    public static void selectionSortByName(Invenory[] list) {

        int minIndex;
        Invenory temp;

        for (int x = 0; x < list.length - 1; x++) {

            minIndex = x;

            for (int i = x + 1; i < list.length; i++) {
                if (list[i].getItemName().compareToIgnoreCase(list[minIndex].getItemName()) < 0) {
                    minIndex = i;
                }
            }

            //swap
            temp = list[x];
            list[x] = list[minIndex];
            list[minIndex] = temp;

        }
    }

    //binary search method
    public static int binarySearchRecursion(Invenory[] list, int leftIndex, int rightIndex, String key) {

        int middle = (leftIndex + rightIndex) / 2;

        int foundIndex = -1;

        if (list[middle].getItemName().compareToIgnoreCase(key) == 0) {
            foundIndex = middle; //found it
        } else if (key.compareToIgnoreCase(list[middle].getItemName()) < 0) {
            if (leftIndex <= middle - 1) {
                foundIndex = binarySearchRecursion(list, leftIndex, middle - 1, key); //recurstion
            }
        } else {
            if (rightIndex >= middle + 1) {
                foundIndex = binarySearchRecursion(list, middle + 1, rightIndex, key); //recursion
            }
        }

        return foundIndex;
    }

    //quick sort method
    public static void quickSort(Invenory [] list, int left, int right) {
        if (left < right) {
            int q = partition(list, left, right);
            quickSort(list, left, q);
            quickSort(list, q + 1, right);
        }
    }

    //partition method
    public static int partition(Invenory[] list, int left, int right) {

        String x = list[left].getItemName(); //piviot
        int i = left - 1;
        int j = right + 1;

        while (true) {

            j--;
            while (list[j].getItemName().compareToIgnoreCase(x) > 0) {
                j--;
            }

            i++;
            while (list[i].getItemName().compareToIgnoreCase(x) > 0 ) {
                i++;
            }

            if (i < j) {
                Invenory temp = list[j];
                list[j] = list[i];
                list[i] = temp;
            } else {
                return j;
            }

        }//end while

    }

}//end class
