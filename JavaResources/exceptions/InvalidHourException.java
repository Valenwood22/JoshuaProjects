public class InvalidHourException extends Exception {

    private String message;
    
       //constructor
    public InvalidHourException() {
        this("Hours must be between 0 and 12.");
    }
    
    public InvalidHourException( String m ) {
        this.message = m;
    }
    
    public String getMessage() {
        return message;
    }
    
    public String toString() {
        return message;
    }

}//end class

