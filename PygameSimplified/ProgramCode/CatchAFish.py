#Author Fatima Abukar

import pygame
import random,os
  
class Fish(pygame.sprite.Sprite):
    
    def __init__(self, image=None):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
    

    # Reset position to the top of the screen, at a random x location.
    #all fishes come from the same position    
    def position(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(700-20)
        
    def swim(self):
        # Move fish down one pixel
        self.rect.y += 1
        # If fish is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.position()

    # Called each frame, overrides Pygames sprite classes' update method
    def update(self):
        self.swim()

#Shark class inherits the fish class
class Shark(Fish):
    def hunt(self):
        posx,posy = pygame.mouse.get_pos()
        self.rect.x=posx
        self.rect.y=posy
        
    def update(self):
        self.hunt()

#Clown fish class inherits the fish class
class ClownFish(Fish):
    def update(self):
        self.swim()

# Set the world for the fish
class World(object):
    def __init__(self):
        self.screen_width=630
        self.screen_height=390
        self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])
        self.background_img=pygame.image.load("images/sea.png")
    
        
#--------------------------------------------------------------------#
                #Client, classes are used below        
#--------------------------------------------------------------------#
pygame.init()

fishWorld=World()

#create a sprite group
goldfish_list = pygame.sprite.Group()
clownfish_list = pygame.sprite.Group()

# This is a list of every sprite. All goldfishes and the player fishes as well.
all_sprites_list = pygame.sprite.Group()
  
for i in range(30):
    goldfish = Fish("images/Goldfish.png")
    # Set a random location for the fish
    goldfish.rect.x = random.randrange(fishWorld.screen_width)
    goldfish.rect.y = random.randrange(fishWorld.screen_height)
    goldfish_list.add(goldfish)
    all_sprites_list.add(goldfish)
      
      
#create the shark
shark = Shark("images/shark.png")
all_sprites_list.add(shark)

for i in range(5):
    clown=ClownFish("images/clownfish.png")
    # Set a random location for the clown fish
    clown.rect.x = random.randrange(fishWorld.screen_width)
    clown.rect.y = random.randrange(fishWorld.screen_height)
    clownfish_list.add(clown)
    all_sprites_list.add(clown)
  
clock=pygame.time.Clock()

#set teh score
score = 0
  
font = pygame.font.Font(None,30)
while True:
    for event in pygame.event.get():
        # If user clicked X button on window
        if event.type == pygame.QUIT:
            pygame.quit()
            
    #draw the fish world
    fishWorld.screen.blit(fishWorld.background_img,(0,0))
    
    score_text=font.render('Score: '+str(score), 1,[0,0,0])
    fishWorld.screen.blit(score_text,(0,10))

    all_sprites_list.update()

    #Check for sprite collisions
    goldfish_hit_list = pygame.sprite.spritecollide(shark, goldfish_list, False)  
    clownfish_hit_list = pygame.sprite.spritecollide(shark, clownfish_list, False)

    
    for goldfish in goldfish_hit_list:
        score +=1
        goldfish.position()
        
    for clownfish in clownfish_hit_list:
        score +=10
        clownfish.position()
        
    #draw the sprites          
    all_sprites_list.draw(fishWorld.screen) 
    clock.tick(20)
    pygame.display.flip()
  

