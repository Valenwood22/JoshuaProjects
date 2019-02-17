
/**
 *
 * @author lt2025vt
 */
public class Cat extends Pet{
    
    private String bodyType;

    public Cat() {
    }

    public Cat(String bodyType, String name, String breed, double weight, int age) {
        super(name, breed, weight, age);
        this.bodyType = bodyType;
    }

    public String getBodyType() {
        return bodyType;
    }

    public void setBodyType(String bodyType) {
        this.bodyType = bodyType;
    }
    
    //overide talk method
    public String talk() {
        return  "Meow, meow, meow";
    }

    @Override
    public String toString() {
        return super.toString() + "Body Type: " + bodyType;
    }
}
