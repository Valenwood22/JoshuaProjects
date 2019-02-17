/**
 *
 * @author lt2025vt
 */
public class BasePlusCommissionEmployee extends CommissionEmployee {

    private double baseSalary;

    public BasePlusCommissionEmployee() {
    }

    public BasePlusCommissionEmployee(double baseSalary, double sales, double comissionRate, int id, String firstName, String lastName) {
        super(sales, comissionRate, id, firstName, lastName);
        this.baseSalary = baseSalary;
    }

    public double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(double baseSalary) {
        this.baseSalary = baseSalary;
    }
    
    //override earnings method
    public double earnings() {
        return this.baseSalary * this.earnings();
    }
    
    @Override
    public String toString() {
        return super.toString() + "\n" +
               "Base Salary: $" + baseSalary;
    }
    
}
