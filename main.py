import pygame
from constants import * 
from player import * 

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0.0 
    print(type(dt))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_one = Player(x, y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((142,84,85))
        player_one.update(dt)
        player_one.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    



if __name__ == "__main__":
    main()
