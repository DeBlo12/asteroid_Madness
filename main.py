import pygame
import sys
from constants import * 
from player import * 
from asteroid import *
from asteroidfield import *
from shot import *

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

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()



    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    Shot.containers = (shot_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    asteroid_field = AsteroidField()

    player_one = Player(x, y)
    



    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

       
        for item in updateable_group:
            item.update(dt)

        for asteroid in asteroid_group:
            if asteroid.isColliding(player_one):
                print("Collision detected")
                sys.exit()
            
            for bullet in shot_group:

                if asteroid.isColliding(bullet):
                    bullet.kill()
                    asteroid.split()


        
        screen.fill((142,84,85))
        
        for drawable in drawable_group: 
            drawable.draw(screen)

    
       
        pygame.display.flip()

        # Limit Framerate to 60 FPS 
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
