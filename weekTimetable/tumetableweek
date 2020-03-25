/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package timetable;
import java.util.HashMap; 
import java.util.Map; 
  

import static com.sun.javafx.animation.TickCalculation.sub;

/**
 *
 * @author Lenovo
 */
public class Tumetableweek {
    
  int  slots = 8;
int halfslot = 4;
String subjects[] =new String[] {"DS","CCNS","ADSA","CC","PROJECT"};
int maxSubWeek = 4;
int daysInWeek = 4;
     String[] day=new String[16];
     
     
     String[] newEmptyDay()//new empty day
    {
        int min=0;
        int max=slots-1;
       
        for(int x=0;x<slots;x++)
        {
            if(day[x]==null){
                slots = (int)(Math.random() * (max - min + 1) + min);
                
                if((slots==3)||(slots==7))
                      return newEmptyDay();//define 
                
                 day[slots] = "prac";
    day[slots + 1] = "prac";
    
                }
        }
        return day;
        }
     
     
     
     String[] newHalfDay() {
         
         int min=0;
        int max=halfslot-1;
       
        for(int x=0;x<slots;x++)
        {
            if(day[x]==null){
                for(int i=0;i<halfslot&&i<slots;i++)
                {
            day[i]="PROJECT";
             slots = (int)(Math.random() * (max - min + 1) + min);
                }
              
                
            }
        }
   
    if (slots == 3)
            return newHalfDay();
    
    day[slots] = "PRACS";
    day[slots + 1] = "PRACS";
    return day; 
     
            }
     
     
     int isDupSubjectPresent(String[] day){
    for(int subject=0;subject<subjects.length;subject++)
    {
        int c=0;
        
        for(int daySub=0;daySub<day.length;daySub++)
        {
            if(subject==daySub)
                c++;
        }
        if(c>1)
            return subject;
    }
       return 0;
            
     
            }
     
     
     int isSubAssignable(String[] day,String sub)
     {
         int maxCount;
         
         
          if (isDupSubjectPresent(day)!=0)
        maxCount = 1;
    else
        maxCount = 2;
          
    int count = 0;
         
         
        for(int x=0;x<day.length;x++)
        { if (day[x] == sub)
            count = count + 1;
        }
        
    if (count < maxCount)
        return 1;
    else
        return 0;
        
         
     }
   
    String getAssignableSub(String[] day)
    { 
        int min=0;
        int max=(subjects.length)-1;
        
        int subIndex = (int)(Math.random() * (max - min + 1) + min);
        
    String sub;
    sub=subjects[subIndex];
    
    if(isSubAssignable(day,sub)==0)
        return sub;
    else
        return getAssignableSub(day);
                }
    
    String[] assignSlot(String[]cday,String sub,int halfDay)
    {
        
    int slot = 0;
    int min=0;
        int max=halfslot-1;
        int max1=slot-1;
        
    if (halfDay==4)
        slot = (int)(Math.random() * (max - min + 1) + min);
    else
        slot = (int)(Math.random() * (max1 - min + 1) + min);
    
    if (day[slot]!=null)
        return assignSlot(day,sub,halfDay);
    else
        day[slot] = sub;
        return day;
    
                }
    
    
    String[] newDay(int halfDay)
    {
        int lecs;
        
        if(halfDay==0){
        day = newHalfDay();
        lecs = halfslot - 2;}
    else
        { day = newEmptyDay();
        lecs = slots-2;
        }
        
    for(int x=0;x<lecs;x++) {
        day = assignSlot(day,getAssignableSub(day),halfDay);
    }
    return day;
            
    
    }
    
   /* int isDayValid(String []week,String[] day)
     {
        HashMap<String, Integer> Subjectcount = new HashMap<>(); 
        Subjectcount.put("pracs", 0); 
        Subjectcount.put("free", 0); 
        
        for(int x=0;x<subjects.length;x++)
        {
            Subjectcount.put(x,0);
        }
        
     }*/
     
     
     
     
   //Hashmaping
    //mainfunction
    /* access and store the data from the database in hashmap and not array
         1)establish a connection
         2) iterate using .next();
         3) use subject.put(key,value)....

    */
    
    
    
    
}//end of class
