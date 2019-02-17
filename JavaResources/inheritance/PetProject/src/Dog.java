/**
 *
 * @author lt2025vt
 */
public class Dog extends Pet{
    //data members
    private String group;
    
    public Dog(){        
    }
    
    public Dog(String group, String name, String breed, double weight, int age) {
        //invoke the superclass constructor
        super(name, breed, weight, age);
        this.group = group;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    
    //overide talk metod
    public String talk() {
        return "Woof, woof, woof";
    }

    @Override
    public String toString() {
        return super.toString() + "Group: " + group;
    }
    
    
}
