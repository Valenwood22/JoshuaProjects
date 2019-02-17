/**
 *
 * @author hm0481jg
 */
public class Student {
    private String id;
    private String firstName;
    private String lastName;
    private String major;
    private String classification;

    public Student() {
    }

    public Student(String id, String firstName, String lastName, String major, String classification) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.major = major;
        this.classification = classification;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
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

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public String getClassification() {
        return classification;
    }

    public void setClassification(String classification) {
        this.classification = classification;
    }

    @Override
    public String toString() {
        return "\n" + id + " " + firstName + " " + lastName + " " + major + " " + classification;
    }
   
}
