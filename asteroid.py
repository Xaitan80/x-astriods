import pygame
import random
from constants import *
from circleshape import CircleShape
#from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
    
        pygame.draw.circle(surface, "white", self.position,self.radius, 2 )

    def update(self, dt):

        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        first_vector *= 1.2
        second_vector *= 1.2
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = first_vector
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = second_vector
        
    


