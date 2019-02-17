
/**
 *
 * @author Jim Ma
 * Date: 8-28-17
 * Program: Flower.java
 * Description: This is a user-defined class
 */
public class Flower {
    
    //instance variables
    private String name;
    private int petals;
    private double price;
    
    //constructors
    public Flower() {
    }

    public Flower(String name, int petals, double price) {
        this.name = name;
        this.petals = petals;
        this.price = price;
    }
    
    //getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPetals() {
        return petals;
    }

    public void setPetals(int petals) {
        this.petals = petals;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return name + " " + petals + " " + price;
    }
   
}
