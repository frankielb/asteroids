from circleshape import CircleShape
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,width=2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        posv,negv = self.velocity.rotate(angle),self.velocity.rotate(-angle)
        newrad = self.radius - ASTEROID_MIN_RADIUS
        pos = Asteroid(self.position.x,self.position.y,newrad)
        neg = Asteroid(self.position.x,self.position.y,newrad)
        pos.velocity = posv * 1.2
        neg.velocity = negv * 1.2