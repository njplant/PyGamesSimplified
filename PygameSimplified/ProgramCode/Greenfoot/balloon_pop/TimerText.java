import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.awt.Color; 

public class TimerText extends Actor
{
    
    public void act() 
    {
        // Add your action code here.
    }   
   
    public TimerText()  
    {  
        this("");  
    }  
  
    public TimerText(String text)  
    {  
        setText(text);  
    }  
  
    public void setText(String text)  
    {  
        setImage(new GreenfootImage(text, 24, Color.black, new Color(0, 0, 0, 0)));  
    }   
}  

