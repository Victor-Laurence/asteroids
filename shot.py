import pygame # type: ignore
from constants import *
from circleshape import CircleShape

# Shot class
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        #circle(surface, color, center, radius, width=0)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt