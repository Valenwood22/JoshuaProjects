
import java.util.ArrayList;

public class ClassRosterClient {

    public static void main(String[] args) {

        ArrayList<Student> studentList = new ArrayList<Student>();

        studentList.add(new UnderGraduateStudent("Tom Sayer"));
        studentList.add(new UnderGraduateStudent("Joe Smith"));
        studentList.add(new GraduateStudent("Ann Johnson"));
        studentList.add(new UnderGraduateStudent("Mary Jane"));
        studentList.add(new GraduateStudent("Ben Moore"));

        int[] scoreList1 = {78, 80, 76};
        int[] scoreList2 = {90, 97, 87};

        studentList.get(0).setTestList(scoreList2);
        studentList.get(1).setTestList(scoreList1);
        studentList.get(2).setTestList(scoreList2);
        studentList.get(3).setTestList(scoreList2);
        studentList.get(4).setTestList(scoreList1);

        int count = 0;
        //[eocess the srinemtLine poltmorphivalls
        for (int i = 0; i < studentList.size(); i++) {
            studentList.get(i).calculateGrade();

            System.out.println(studentList.get(i).toString() + "\n");

            if (studentList.get(i) instanceof UnderGraduateStudent) {
                count++;
            }
        }
        
        System.out.println ("\nNumber of undergraduate Students: " + count);
    }

    
}
