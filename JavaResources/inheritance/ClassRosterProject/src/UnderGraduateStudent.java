
/**
 *
 * @author lt2025vt
 */
public class UnderGraduateStudent extends Student {

    public UnderGraduateStudent(String name) {
        super(name);
    }

    //overide calculateGrade();
    public void calculateGrade() {

        int sum = 0;

        int[] temp = this.getTestList();

        for (int i = 0; i < NUM_OF_TESTS; i++) {
            sum += temp[i];
        }

        if (sum / NUM_OF_TESTS >= 70) {
            setGrade("Pass");
        } 
        else {
            setGrade("No Pass");
        }
    }
}
