
import java.util.*;

public class BlurbGenerator {

   private Random rand;
   
   //constructor
   public BlurbGenerator() {
      rand = new Random();
   }
   
   public String generateBlurb() {
   
      StringBuilder blurb = new StringBuilder();
      blurb.append( getWhoozit() );
      blurb.append( getMultipleWhatzits() );
      
      return blurb.toString();
      
   }
   
   public String getWhoozit() {
   
      StringBuilder whoozit = new StringBuilder();
      whoozit.append("x");
      whoozit.append( getYs() );
      
      return whoozit.toString();
   
   }
   
   public String getYs() {
   
      StringBuilder y = new StringBuilder();
      
      boolean stop = rand.nextBoolean(); //random boolean
      
      if(!stop) {
         y.append( getYs() ); //recursive call to getYs()
      }
      else {
         return y.toString();
      }
      
      y.append("y");
      
      return y.toString();
   
   }
   
   public String getMultipleWhatzits() {
   
      StringBuilder whatzits = new StringBuilder();
      
      whatzits.append( getWhatzit() );
      
      boolean stop = rand.nextBoolean();
      
      if(!stop) {
         whatzits.append( getMultipleWhatzits() );
      }
      else {
         return whatzits.toString();
      }
      
      return whatzits.toString();
   
   }
   
   public String getWhatzit() {
   
      StringBuilder whatzit = new StringBuilder();
      
      whatzit.append("q");
      
      boolean flag = rand.nextBoolean();
      
      if(flag){
         whatzit.append("z");
      }
      else{
         whatzit.append("d");
      }
      
      whatzit.append( getWhoozit() );
      
      return whatzit.toString();
   }


   public static void main(String[] args) {
   
      BlurbGenerator alien = new BlurbGenerator();
      
      System.out.println( alien.generateBlurb() );
      
   }//end main 
        
}//end class