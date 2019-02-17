/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lt2025vt
 */
public class GraduateStudent extends Student{

  public GraduateStudent(String name) {
        super(name);
    }
    
    //overide calculateGrade();
    public void calculateGrade(){
        
        int sum = 0;
        
        int [] temp = this.getTestList();
        
        for(int i=0; i<NUM_OF_TESTS; i++) {
            sum += temp[i];
        }
        
        if( sum / NUM_OF_TESTS >= 80 ){
            setGrade("Pass");
        }
        else {
            setGrade("No Pass");
        }
        
    }
      
    
}
