import pygame

# principle of game:
# loop : process input -> update game -> render

SCREEN_SIZE = (500,600)


# initailize game and create windows

def initail():
    pygame.init()
    screen = pygame.display.set_mode((500,600))

# Defining main function
def main():
    print("----------start the game----------")
    initail()
    # whether running game
    running = True

    # loop for the game
    while running:
        # get input from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

  

  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()