
/**
 *
 * @author lt2025vt
 */

public class HourlyEmployee extends Employee {
    private double hoursWorked;
    private double baseWage;

    public HourlyEmployee() {
    }

    public HourlyEmployee(double hoursWorked, double baseWage, int id, String firstName, String lastName) {
        super(id, firstName, lastName);
        this.hoursWorked = hoursWorked;
        this.baseWage = baseWage;
    }

    public double getHoursWorked() {
        return hoursWorked;
    }

    public void setHoursWorked(double hoursWorked) {
        this.hoursWorked = hoursWorked;
    }

    public double getBaseWage() {
        return baseWage;
    }

    public void setBaseWage(double baseWage) {
        this.baseWage = baseWage;
    }
    
    public double ernings() {
        double pay;
        
        if(hoursWorked <= 40) {
            pay = hoursWorked * baseWage;
        }
        else {
            pay = 40 * baseWage + (hoursWorked - 40) * baseWage * 1.5;
        }
        return pay;
    }
    

    @Override
    public String toString() {
        return super.toString() + "\n" +
               "Hours Worked: " + hoursWorked + "\n" +
               "Base Wage: " + baseWage;
    }
}
