from circleshape import *

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
         