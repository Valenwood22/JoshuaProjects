
/**
 *
 * @author lt2025vt
 */
public class PayrollClient {

    public static void main(String [] args) {
        
        //Employee e1 = new Employee(10001, "Jon", "Doe");
        
        CommissionEmployee c1 = new CommissionEmployee(8000, 0.15, 10002, "Tom", "Sawyer");
        
        BasePlusCommissionEmployee b1 = new BasePlusCommissionEmployee( 1000, 8000, 0.05, 10003, "Joe", "Smith");

        //System.out.println( e1 );
        //System.out.println("Earnings: $" + e1.earnings() + "\n");
        
        System.out.println( c1 );
        System.out.println("Earnings: $" + c1.earnings() + "\n"); 
        
        System.out.println( b1 );
        System.out.println("Earnings: $" + b1.earnings() + "\n"); 
        
        
    }   
    
}
