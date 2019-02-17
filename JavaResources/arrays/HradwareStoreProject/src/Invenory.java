/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lt2025vt
 * Date: 1-8-18
 * Name: Inventory.java
 * Description:
 */
public class Invenory {
    
    //data members - instance variables
    private int pid;
    private String itemName;
    private int numberOfPrices;
    private double unitPrice;
    
    //default constructor
    public Invenory() {
        //defult values will be assigned to 
        //the data members
    }
    
    //overloaded constructor

    public Invenory(int pid, String itemName, int numberOfPrices, double unitPrice) {
        this.pid = pid; //this.pid reffers to the data member where as pid is the 
        this.itemName = itemName;
        this.numberOfPrices = numberOfPrices;
        this.unitPrice = unitPrice;
    }
    
    //getters and setters

    public int getPid() {
        return pid;
    }

    public void setPid(int pid) {
        this.pid = pid;
    }

    public String getItemName() {
        return itemName;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public int getNumberOfPrices() {
        return numberOfPrices;
    }

    public void setNumberOfPrices(int numberOfPrices) {
        this.numberOfPrices = numberOfPrices;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }
    
    public double calculateInStockValue() {
        return this.numberOfPrices * this.unitPrice;
    }
    
    //toString method

    @Override
    public String toString() {
        return String.format("%-5d %-16s %,-8d $%,-9.2f $%,-15.2f",
                            pid, itemName, numberOfPrices, unitPrice, 
                            this.calculateInStockValue());
    }
    
    
    
}
