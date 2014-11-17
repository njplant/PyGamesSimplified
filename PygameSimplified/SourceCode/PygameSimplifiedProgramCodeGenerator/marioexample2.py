#import 
from PGS.PygameSimplified import*

marioWorld= World(100,200)
marioWorld.set_background("images/mbg.jpg")
mario= Actor()

mario.set_image("images/mario.png")

mario.set_location(100,100)







running = True
#while loop
while running:
    mario.update()

    #---Enter your game logic below here!---

    marioWorld.draw_background(0,0)
    marioWorld.draw_actor(mario,mario.x,mario.y)

   
    Event.exit_game(running)
    Event.update()
    










   



        





    
