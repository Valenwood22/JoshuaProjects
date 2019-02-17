
import java.util.ArrayList;

/**
 *
 * @author lt2025vt
 */
public class PetClient {

    public static void main(String [] args) {        
        
            //polymorphic reference
        ArrayList<Pet> petList = new ArrayList<Pet>();
        
            //add subclass objects to the petList
        petList.add(new Dog("Sporting Group", "Frankie", "Bulldog", 45, 6));
        petList.add(new Cat("Round", "Annie", "Bombay", 8, 4));
        petList.add(new Cat("Round", "Mary", "Asian", 10, 5));
        petList.add(new Dog("Sporting Group", "Jimmy", "Terrier", 15, 5));
        petList.add(new Cat("Unknown", "Kay", "Bombay", 8, 4));

            //procss the petList polymorphically
        int cat_count = 0;
        
        for(int  i=0; i<petList.size(); i++) {
            System.out.println( petList.get(i));
            System.out.println( petList.get(i).talk() );
            System.out.println();
            
            if(petList.get(i) instanceof Cat) {
                cat_count ++;
            }
        }
        
        System.out.println("Cat count: " + cat_count);
        
        
        /*
        Pet p1 = new Pet("Jimmy", "Unknown", 23.0, 4);
        
        Dog d1 = new Dog("Sporting Group", "Frankie", "Bulldog", 45, 6);
        
        Cat c1 = new Cat("Round", "Annie", "Bombay", 8, 4);
        
        d1.setAge(7);
         
        System.out.println(p1.toString());
        System.out.println(p1.talk());
        
        System.out.println(d1.toString());
        System.out.println(d1.talk());
        
        System.out.println();
        
        System.out.println(c1.toString());
        System.out.println(c1.talk());
        */
                
    }
}