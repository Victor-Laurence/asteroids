from constants import *
from circleshape import *

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        #polygon(surface, color, points, width=0) 
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, COUNTER_CLOCKWISE)
        if keys[pygame.K_d]:
            self.rotate(dt, CLOCKWISE)

    def rotate(self, dt, direction = CLOCKWISE):
        self.rotation += PLAYER_TURN_SPEED * dt * direction