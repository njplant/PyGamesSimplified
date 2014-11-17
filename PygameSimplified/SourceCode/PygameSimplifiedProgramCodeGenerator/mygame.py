from PGS.PygameSimplified import *
# part 2. create our world
paintworld = World(800,600)

# part 2.1. create our actor
redBrush=Actor()
blueBrush=Actor()
orangeBrush = Actor()
greenBrush = Actor()
liverpool = Actor()
# part 4. fill our world with a white background
paintworld.window.fill((255,255,255))

# part 5. set the image of our paint brush
redBrush.set_image("images/red.png")
blueBrush.set_image("images/blue.png")
orangeBrush.set_image("images/orange.png")
greenBrush.set_image("images/green.png")
liverpool.set_image("images/lfc.png")

default_brush = redBrush

redBrush.set_location(25,0)
blueBrush.set_location(95,0)
orangeBrush.set_location(165,0)
greenBrush.set_location(235,0)
liverpool.set_location(400,0)

# part 6. while the game is running execute the code below
while True:
    
    # part 7. update    
    Event.update()
    paintworld.update()
    redBrush.update()
    blueBrush.update()
    orangeBrush.update()
    greenBrush.update()
    liverpool.update()

    # part 8. set the mouse position    
    mousex,mousey= Event.mouse_pos
    
    # part 9. set the position of the mouse cursor    
    Event.set_CursorPosOnImage(60,60)
    Event.set_MouseCursorPos(mousex,mousey)

    paintworld.draw_actor(redBrush, redBrush.x,redBrush.y)
    paintworld.draw_actor(blueBrush, blueBrush.x,blueBrush.y)
    paintworld.draw_actor(orangeBrush,orangeBrush.x,orangeBrush.y)
    paintworld.draw_actor(greenBrush,greenBrush.x,greenBrush.y)
    paintworld.draw_actor(liverpool,liverpool.x,liverpool.y)
    
    if Event.contains("exit"):
        Event.quit_game()
        
    elif Event.mouse_down("Button1"):
        #red
        if redBrush.collide_point(Event.mouse_pos):
            default_brush = redBrush
            
        #blue
        if blueBrush.collide_point(Event.mouse_pos):
            default_brush = blueBrush
        #orange
        if orangeBrush.collide_point(Event.mouse_pos):
            default_brush = orangeBrush        
                
        #green
        if greenBrush.collide_point(Event.mouse_pos):
            default_brush = greenBrush
            
        ##liverpool    
        if liverpool.collide_point(Event.mouse_pos):
            default_brush = liverpool

            
        # part 10. draw the image at where your mouse is
        paintworld.draw_actor(default_brush, mousex, mousey)

    











