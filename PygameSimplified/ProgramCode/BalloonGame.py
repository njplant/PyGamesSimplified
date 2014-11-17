#make importations
from PGS.PygameSimplified import *
 
# Set the height and width of the screen
world = World(700,400)
balloon = Actor()
firedArrow = Actor()
arrow = Actor()
mytimer = Timer()
score_text = Text(world)
timer_text = Text(world)
balloon_sound = Sound()

arrow.set_image("images/arrow.png")
world.set_tile_background("images/background.png")
balloon_sound.set_sound("sound/balloon-pop.wav")

#make actor groups
balloon.generate_rand_actors(10,"images/balloon.png",world)
firedArrow.make_actor_group()

arrow.set_location(700,350)
score=0

#Main Loop 
while True:
    Event.update()
    arrow.update()
    balloon.update_actors()

    
    mousex, mousey = Event.mouse_pos
    arrow.x = mousex
    
    for ball in balloon:
        ball.move_by(0,1)
        #if the balloon goes of screen, add two balloons so we dont run out of balloons        
        if ball.y == world.height:
            balloon.generate_rand_actors(2,"images/balloon.png", world)

    if Event.contains("exit"):
        Event.quit_game()
        
    # Fire a bullet if the user clicks the mouse button
    elif Event.mouse_down("Button1"):
        firedArrow.set_image("images/arrow.png") 
        firedArrow.update()
        # Set the bullet so it is where the arrow is
        firedArrow.x = arrow.x
        firedArrow.y = arrow.y
        # Add the bullet to the lists
        firedArrow.add_actor(firedArrow)
        
        
    # making an update between adding and removing the bullet. 
    firedArrow.update()
    
    for arr in firedArrow:
        firedArrow.move_by(0,-10)
        if balloon.collide_group(arr):
            score = score+1
            balloon_sound.play()

    #if the length of the balloon list is less than 7 re-draw it.    
    if balloon.actor_group_length()<=10:
        balloon.generate_rand_actors(10,"images/balloon.png",world)
       
    world.draw_tile_background(100,100)
    world.draw_actor(arrow, arrow.x, arrow.y)
    balloon.draw_actors(world.window)
    firedArrow.draw_actors(world.window)
    
    mytimer.decrement_timer(20)
    if mytimer.seconds ==0:
        score= 0
    
    #set texts
    timer_text.set_text( "Timer:"+str(mytimer.seconds))
    timer_text.draw_text(world.width/2,40)
        
    score_text.set_text("Score: "+ str(score))
    score_text.draw_text(world.width/2,10)

        
    
 
 
     
    

