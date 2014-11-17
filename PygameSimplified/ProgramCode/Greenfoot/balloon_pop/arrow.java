import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
public class arrow extends Actor
{
    
    private int speed=0;
    public void act() 
    {
        // Add your action code here.
        MouseInfo mouse = Greenfoot.getMouseInfo();
        if (mouse !=null)
        {
            //move(speed);
            if(Greenfoot.mouseClicked(null))
            {
                getWorld().addObject(new firedArrow(getRotation()) ,getX(),getY());
                setLocation(mouse.getX(),this.getY());
        
            }
        }
        of_screen();
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
