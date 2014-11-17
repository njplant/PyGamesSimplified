#CatchaFish Using Pygame Simplified
#make importations
from PGS.PygameSimplified import *

fishWorld = World(630,390)

clownFish = Actor()
goldFish = Actor()
shark= Actor()
badrock= Actor()
score_text = Text(fishWorld)
mytimer = Timer()
timer_text = Text(fishWorld)

badrock.set_image("images/badrock1.png")
shark.set_image("images/shark.png")
fishWorld.set_background("images/sea.png")

goldFish.generate_rand_actors(20,"images/goldfish.png",fishWorld)
clownFish.generate_rand_actors(4,"images/clownfish.png",fishWorld)
badrock.generate_rand_actors(4,"images/badrock1.png",fishWorld)
shark.set_location(100,100)
score=0

while True:
    
    shark.update()
    Event.update()
    
    clownFish.update_actors()
    goldFish.update_actors()
    badrock.update_actors()
    mousex,mousey=Event.mouse_pos
    
    if Event.contains("exit"):
        Event.quit_game()
        
    #set the x and y of shark to the position of mouse    
    shark.set_location(mousex,mousey)
    
    for fishes in goldFish:
        fishes.move_by(0,2)
        if fishes.y == 410 or goldFish.actor_group_length()<=10:
             goldFish.generate_rand_actors(5,"images/goldfish.png", fishWorld)
             clownFish.generate_rand_actors(2,"images/clownfish.png",fishWorld)
             badrock.generate_rand_actors(2,"images/badrock1.png",fishWorld)
        
    if goldFish.collide_group(shark):
        score=score+1

    for clown in clownFish:
        clown.move_by(0,2)
        
    if clownFish.collide_group(shark):
        score=score+10
        
    if badrock.collide_group(shark):
        score=score-10


    mytimer.decrement_timer(10)
  

    fishWorld.draw_background(0,0)
    fishWorld.draw_actor(shark, mousex,mousey)
    goldFish.draw_actors(fishWorld.window)
    clownFish.draw_actors(fishWorld.window)
    badrock.draw_actors(fishWorld.window)

    score_text.set_text("Score: "+ str(score))
    score_text.draw_text(fishWorld.width/2,10)
    timer_text.set_text( "Timer:"+str(mytimer.seconds))
    timer_text.draw_text(fishWorld.width/2,40)

    
   
    


