import pygame
from circleshape import CircleShape
import constants as c


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt