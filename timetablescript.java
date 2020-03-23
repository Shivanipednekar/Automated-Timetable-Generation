/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package timetable;
import java.utils.*;
/**
 *
 * @author Lenovo
 */
public class timetablescript {
    int slots=8;
    String[] subj=new String[]{"DS","CCNS","ADSA","CC"}; //STATIC INPUT TO CHECK
    
   // String[] subjects=new String[20]; //data frpm database
    
    String[] newempday()//new empty day
    {
        int min=0;
        int max=slots-1;
        String[] day=null;
        for(int x=0;x<slots;x++)
        {
            if(day[x]==null){
                slots = (int)(Math.random() * (max - min + 1) + min);
                
                if((slots==3)||(slots==7))
                        return assignPracs(); //define assign pracs
                
                 day[slots] = "prac";
    day[slots + 1] = "prac";
    
                
        }
        }
        
        for(int i=0;i<day.length;i++)
             System.out.print(day[i]);
        
        return day;
    }
    
    int isSubAssignable(String[] day,String[] sub)
    {
         int count = 0;
    for(int x=0;x<day.length;x++)
    {
        
        if(day[x]==sub[x])
            count = count + 1;
    }
    if (count < 2)
        return 1;
    else
        return 0;
    }
   
    
    String[] getAssignableSub(String[] day){
        int sIndex;
        int min=0;
        int max=subj.length;
        
        sIndex=(int)(Math.random() * (max - min + 1) + min);
        //String[] s1=new String[16];
        String s2=subj[sIndex];
        
        if(isSubAssignable(day,subj)) //define
        return subj;
    else
        return getAssignableSub(day);

        
    }
   
    String[] assignSlot(String[] day,String[] sub){
        
        int min=0;
        int max=slots-1;
        
        slots=(int)(Math.random() * (max - min + 1) + min);
    
    if (day[slots]=null)             //getting an error here
        return assignSlot(day,sub);
    else
        day[slots] = sub;  //error
        return day;
                }
    
    String[] newDay(){
    String[]day =new String[10];
    day=newempday();
    
    for(int x=0;x<slots-1;x++)
    {
         day= assignSlot(day,getAssignableSub(day));
    }
   
       
    return day;


        }

    //main class
    
}//closing of class
