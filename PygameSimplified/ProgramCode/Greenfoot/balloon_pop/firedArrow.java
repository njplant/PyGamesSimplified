import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.List;
/**
 * Write a description of class firedArrow here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class firedArrow extends Actor
{
    //private int direction;
   
    /**
     * Act - do whatever the firedArrow wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        // Add your action code here.
        move(5);
        of_screen();
        if (getWorld() != null)
            collide_with_ballon();
        
            
        
        
    }    
    public firedArrow(int dir)
    {
        dir = -90;
        setRotation(dir);
    }
    
    
    public void collide_with_ballon()
    {
        Actor balloon=getOneIntersectingObject(balloon.class);
        if(balloon !=null)
        {
            ((balloon)balloon).pop();
            getWorld().removeObject(balloon);
            getWorld().removeObject(this);
            Greenfoot.playSound("balloon-pop.wav");
            
      
        }
        
        
    }  
        
    
    public void of_screen()
    {
        if(getX()>=getWorld().getWidth()-1)
            getWorld().removeObject(this);
        else if (getX() <=1)
            getWorld().removeObject(this);
        else if (getY() >=getWorld().getHeight()-1)
            getWorld().removeObject(this);
        else if(getY() <=1)
            getWorld().removeObject(this);
    }
}
