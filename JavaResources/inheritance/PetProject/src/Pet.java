/**
 *
 * @author lt2025vt
 */
public abstract class Pet {
    //data members
    private String name;
    private String breed;
    private double weight;
    private int age;

    public Pet() {
    }

    public Pet(String name, String breed, double weight, int age) {
        this.name = name;
        this.breed = breed;
        this.weight = weight;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
        
    /*
       //it is for polymorphism
    public String talk() {
        return "Don't know how to talk";
    }
    */
    
    abstract public String talk();
    
    @Override
    public String toString() {
        return ("Name: " + name + "\n" +
                "Breed: " + breed + "\n" +
                "Weight: " + weight + "\n" +
                "Age: " + age + "\n");
    }
}//end main
