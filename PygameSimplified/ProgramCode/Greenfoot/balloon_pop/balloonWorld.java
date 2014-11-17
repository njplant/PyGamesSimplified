import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class balloonWorld extends World
{
    Counter counter = new Counter("Balloon score:");
    TimerText timerText= new TimerText();
    
    private int timer=20;
    private int score;
    private int timer2 =20;
    
   
    public void countPop()
    {
        counter.add(1);
        
    }
    public balloonWorld()
    {    
       // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
       super(600, 400, 1); 
       timerText.setText("Time left: " + (timer));  
       populate();
        
    }
    private void populate()
    {
        
        addObject(timerText,300,50 );  
        addObject(counter,340, 20);
        addObject(new arrow(),300,360);
        counter.getValue();
        
    }
    public void act() 
    {
        
        if(Greenfoot.getRandomNumber(100) < 3) {
            addObject(new balloon(), Greenfoot.getRandomNumber(700), 600);   
        }
        if (timer2== 0)  
        {  
            timer--;  
            timerText.setText("Time left: " + (timer));
            if (timer== 0)
            {
              timer = 20;
              
            }
        }
        timer2 =(timer2 +1)%50;
        
    }
    
   
}
