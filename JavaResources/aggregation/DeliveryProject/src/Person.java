
/**
 *
 * @author lt2025vt
 */
public class Person {
    //data members
    private String firstName;
    private String lastName;
    private String address;
    private String city;
    private String state;
    private String zipCode;

    public Person() {
    }
    
    public Person(String firstName, String lastName, String address, String city, String state, String zipCode) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.address = address;
        this.city = city;
        this.state = state;
        this.zipCode = zipCode;
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

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getZipCode() {
        return zipCode;
    }

    public void setZipCode(String zipCode) {
        this.zipCode = zipCode;
    }

    @Override
    public String toString() {
        return (firstName + " " + lastName + " " + address + " " + 
               city + " " + state + " " + zipCode);
    }
    
    
}
