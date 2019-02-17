
/**
 *
 * @author lt2025vt
 */
public class DeliveryClientProgram {
    
    public static void main(String [] args) {
        
        Parcel p1;
        
        p1 = new Parcel( 20090, 12.56, 5.4, 
                         new Person("Jon", "Doe", "123 Main St.", "SomeCity", "MN", "99121"),
                         new Person("Mary", "Jane", "888 2nd St.", "AnotherCity", "MN", "99421"),
                         new Date(1, 24, 2018),
                         null );
        
        System.out.println( p1 );
        System.out.println("Delivery Cost: $" + p1.calculateDeliveryCost());
        System.out.println();
        
        //Change the delivery date
        p1.setDeliveryDate(new Date(1, 28, 2018));
        
        //print the recipient's name
        System.out.println("Recipient: " + 
                           p1.getRecipient().getFirstName() + " " +
                           p1.getRecipient().getLastName());
        
        System.out.println( p1 );
        System.out.println("Delivery Cost: $" + p1.calculateDeliveryCost());
        System.out.println();
        
    }//end main
    
}//end class
