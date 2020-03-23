/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package timetable;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.*;

/**
 *
 * @author Lenovo
 */
public class Timetable {

    
  public static void main(String[] args) {
       
        
        try{
         Class.forName("oracle.jdbc.driver.OracleDriver");
    
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","SHIVANIPEDNEKAR","root");
    
    Statement stmt=con.createStatement();
      
               ResultSet rs=stmt.executeQuery("Select * from SUBJECTS");
              // String p=rs;
              while(rs.next()) {

    for (int column = 1; column <= 7; column++) {

        if(column > 1) System.out.print(", ");
        System.out.print(rs.getString(column));
        
    }
}
        }
            
            
            
        
        catch(Exception e){
            System.out.println("Error: "+e);
        }
        //return 0;
    }
    
}

//class Last{
   

/*public static void main(String[] args)
{
     DataInputStream inst = new DataInputStream(System.in);
public static void main(String[] args)
do{
    System.out.println("Press 1 to retrieve BE course details");
    int p=Integer.parseInt(r.readline());
}
}
}*/