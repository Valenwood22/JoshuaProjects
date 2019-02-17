
import java.util.ArrayList;

/**
 *
 * @author hm0481jg
 */
public class Course {
    //data members
    private String courseNummber;
    private String courseTitle;
    private int creditHours;
    private String location;
    
    private Date startDate;
    private Date endDate;
    private Instructor teacher;
    private Book textBook;
    private ArrayList<Student> studentList;
    
    //constructor

    public Course() {
    }

    public Course(String courseNummber, String courseTitle, int creditHours, String location, Date startDate, Date endDate, Instructor teacher, Book textBook, ArrayList<Student> studentList) {
        this.courseNummber = courseNummber;
        this.courseTitle = courseTitle;
        this.creditHours = creditHours;
        this.location = location;
        this.startDate = startDate;
        this.endDate = endDate;
        this.teacher = teacher;
        this.textBook = textBook;
        this.studentList = studentList;
    }

    public String getCourseNummber() {
        return courseNummber;
    }

    public void setCourseNummber(String courseNummber) {
        this.courseNummber = courseNummber;
    }

    public String getCourseTitle() {
        return courseTitle;
    }

    public void setCourseTitle(String courseTitle) {
        this.courseTitle = courseTitle;
    }

    public int getCreditHours() {
        return creditHours;
    }

    public void setCreditHours(int creditHours) {
        this.creditHours = creditHours;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Date getStartDate() {
        return startDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public void setEndDate(Date endDate) {
        this.endDate = endDate;
    }

    public Instructor getTeacher() {
        return teacher;
    }

    public void setTeacher(Instructor teacher) {
        this.teacher = teacher;
    }

    public Book getTextBook() {
        return textBook;
    }

    public void setTextBook(Book textBook) {
        this.textBook = textBook;
    }

    public ArrayList<Student> getStudentList() {
        return studentList;
    }

    public void setStudentList(ArrayList<Student> studentList) {
        this.studentList = studentList;
    }

    @Override
    public String toString() {
        return ("Course Nummber: " + courseNummber + "\n" +
                "Course Title: " + courseTitle + "\n" +
                "Credit Hours: " + creditHours + "\n" +
                "Location: " + location + "\n" +
                "Start Date: " + startDate + "\n" +
                "End Date: " + endDate + "\n" +
                "Teacher: " + teacher + "\n" +
                "Text Book: " + textBook + "\n" +
                "Student List: " + studentList );
    }
     
}
