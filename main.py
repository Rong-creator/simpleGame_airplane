import pygame
import player as p
import rock as r

# principle of game:
# loop : process input -> update game -> render

SCREEN_SIZE = (500,600)
FPS = 60


# initailize game and create windows

def initail():
    pygame.init()
    screen = pygame.display.set_mode((500,600))

    # change caption
    pygame.display.set_caption("Airplane")
    return screen 

def create_sprites_group():
    all_sprites = pygame.sprite.Group()
    player = p.player()
    all_sprites.add(player)
    for i in range(8):
        rock = r.rock()
        all_sprites.add(rock)

    return all_sprites

# Defining main function
def main():
    print("----------start the game----------")
    screen = initail()
    # whether running game
    running = True

    # create clock
    clock = pygame.time.Clock()

    all_sprites = create_sprites_group()

    # loop for the game
    while running:
        # execute FPS times in 1 sec 
        # then limit the number of loops per sec
        clock.tick(FPS)

        # get input from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # update the game

        all_sprites.update()

        # show image or pic
        screen.fill((255,255,255))
        
        
        all_sprites.draw(screen)
        pygame.display.update()
        
    
    # close the windows
    pygame.quit()

  

  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()