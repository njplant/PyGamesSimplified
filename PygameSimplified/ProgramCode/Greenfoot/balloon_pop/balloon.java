import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class balloon here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class balloon extends Actor
{
    /**
     * Act - do whatever the balloon wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */

    public void act() 
    {
        // Add your action code here.
        setLocation(getX(), getY()-1);
        of_screen();
        
        
    }  
    
    public void pop()
    {
        ((balloonWorld) getWorld()).countPop();
       
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
