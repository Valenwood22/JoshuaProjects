/**
 *
 * @author lt2025vt
 */
public abstract class Employee {
    private int id;
    private String firstName;
    protected String lastName;

    public Employee() {
    }

    public Employee(int id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    /*
    public double earnings() {
        return 0.0;
    }
    */
    
    public abstract double earnings();
    
    @Override
    public String toString() {
        return "Employee ID: " + id + "\n" +
               "First Name: " + firstName + "\n" +
               "Last Name: " + lastName;
    }
    
    
    
}