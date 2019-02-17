/**
 *
 * @author lt2025vt
 */
public abstract class Student {
    private String name;
    private int [] testList;
    private String grade;
    
    protected final static int NUM_OF_TESTS=3;

    public Student() {
    }

    public Student(String name) {
        this.name = name;
        this.testList = new int[NUM_OF_TESTS];
        this.grade = "Unknown";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int[] getTestList() {
        return testList;
    }

    public void setTestList(int[] testList) {
        this.testList = testList;
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    
    abstract public void calculateGrade();

    @Override
    public String toString() {
        return "Student Name: " + name + "\n" +
               "Grade: " + grade;
    }
}
