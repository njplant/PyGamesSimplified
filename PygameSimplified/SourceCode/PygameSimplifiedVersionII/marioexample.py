#Author: place your name
#Date: place the date

#Import all the modules in Pygame Simplisfied
from PGS.PygameSimplified import *

#create world
marioworld = World(800,600)

#create actors
mario = Actor()
coin = Actor()
mario_text = Text(marioworld)

#set background of world
marioworld.set_background("images/mbg.jpg")

#set actor images
mario.set_image("images/mario.png")
coin.set_image("images/coin.png")

#set location of actors
mario.set_location(50,510)
coin.set_location(400, 510)

#while game is running
while True:
    
    #update actors    
    mario.update()
    coin.update()
    
    #update events   
    Event.update()

    #check if key is pressed    
    if Event.is_key("down"):
        #move mario        
        mario.move_by(0,4)
    elif Event.is_key("up"):
        mario.move_by(0,-4)
    elif Event.is_key("right"):
        mario.move_by(4,0)
    elif Event.is_key("left"):
        mario.move_by(-4,0)
    
        
    #checks if a key has been pressed.    
    if Event.key_up(K_a):
        #if it has alter the speed.        
        mario.turn(3)
    if Event.key_up(K_d):
        mario.set_speed(7)
    if Event.key_up(K_n):
        mario.set_speed(1)
        
    #draw mario world
    marioworld.draw_background(0,0)
    
    #draw actors    
    marioworld.draw_actor(mario,mario.x,mario.y)
    marioworld.draw_actor(coin,coin.x,coin.y)

    #if user clicks X quit game 
    if Event.contains("exit"):
        Event.quit_game()
    
    #set text    
    mario_text.set_text("MARIO WOOOOOOOO!")
    mario_text.draw_text(0,10)
    mario_text.set_font("Arial",20)
    mario_text.set_colour(0,0,0)

    
    



    
