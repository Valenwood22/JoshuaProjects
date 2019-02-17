/**
 *
 * @author hm0481jg
 */
public class Instructor {
    private String firstName;
    private String lastName;
    private String officeLocation;
    private String officeNumber;
    private String email;

    public Instructor() {
    }

    public Instructor(String firstName, String lastName, String officeLocation, String officeNumber, String email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.officeLocation = officeLocation;
        this.officeNumber = officeNumber;
        this.email = email;
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

    public String getOfficeLocation() {
        return officeLocation;
    }

    public void setOfficeLocation(String officeLocation) {
        this.officeLocation = officeLocation;
    }

    public String getOfficeNumber() {
        return officeNumber;
    }

    public void setOfficeNumber(String officeNumber) {
        this.officeNumber = officeNumber;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return firstName + " " + lastName + " " + officeLocation + 
               " " + officeNumber + " " + email;
    }
    
}
