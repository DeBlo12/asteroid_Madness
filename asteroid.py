from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)

                

    def draw(self, surface, width = 2):
        pygame.draw.circle(surface, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, width)
        
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.x, self.y = self.velocity.x * dt, self.velocity.y * dt
        

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("small asteroid killed")
            return
        
        random_angle = random.uniform(20,50)

        velocity_vector_one = self.velocity.rotate(random_angle)
        velocity_vector_two = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = velocity_vector_one * 1.2
        asteroid_two.velocity = velocity_vector_two * 1.2