
/**
 *
 * @author lt2025vt
 */
public class CommissionEmployee extends Employee {
    
    private double sales;
    private double comissionRate;

    public CommissionEmployee() {
    }

    public CommissionEmployee(double sales, double comissionRate, int id, String firstName, String lastName) {
        super(id, firstName, lastName);
        this.sales = sales;
        this.comissionRate = comissionRate;
        
        //this.firstName = "Some Name";
        //this.lastName = "Changed";
        
        
    }

    public double getSales() {
        return sales;
    }

    public void setSales(double sales) {
        this.sales = sales;
    }

    public double getComissionRate() {
        return comissionRate;
    }

    public void setComissionRate(double comissionRate) {
        this.comissionRate = comissionRate;
    }
    
    //overide ernings method
    public double earnings() {
        return this.comissionRate * this.sales;
    }

    @Override
    public String toString() {
        return super.toString() + "\n" +
               "Sales: $" + sales + "\n" +
               "Comission Rate: " + comissionRate;
    }
}
