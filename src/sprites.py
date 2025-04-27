# src/sprites.py
import pygame
import settings
import random
from utils import load_image, cut_spritesheet, load_sound
from utils import resource_path

# Pac-Man class
class Pacman(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        super().__init__()
        image_path = resource_path('assets/images/pacman.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.Vector2(0, 0)  # Direction of movement
        self.speed = 150  # Pacman speed

    def update(self, dt, level):
        # Calculate the new position based on direction and speed
        new_rect = self.rect.copy()
        new_rect.x += self.direction.x * self.speed * dt
        new_rect.y += self.direction.y * self.speed * dt

        eaten_pellet = level.eat_pellet(self.rect.centerx, self.rect.centery)
        if eaten_pellet:
            pass

        # Check for wall collisions and adjust position if needed
        if not level.is_wall(new_rect.x, new_rect.y):
            self.rect.x = new_rect.x
            self.rect.y = new_rect.y
        else:
            # If there's a collision with a wall, stop movement in that direction
            if self.direction.x != 0:
                self.rect.x -= self.direction.x * self.speed * dt
            if self.direction.y != 0:
                self.rect.y -= self.direction.y * self.speed * dt

# Ghost class

class Ghost(pygame.sprite.Sprite):
    def __init__(self, position: tuple, color: str):
        super().__init__()
        self.color = color
        image_path = resource_path(f'assets/images/ghost_{self.color}.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.Vector2(0, 0)
        self.speed = 100

    def update(self, dt, level):
        # Simple AI for random movement (can be improved later)
        if random.random() < 0.01:  # 1% chance to change direction per frame
            self.direction = pygame.Vector2(random.choice([1, -1, 0]), random.choice([1, -1, 0]))

        # Calculate the new position based on direction and speed
        new_rect = self.rect.copy()
        new_rect.x += self.direction.x * self.speed * dt
        new_rect.y += self.direction.y * self.speed * dt

        # Check for wall collisions using the new_rect and adjust position if needed
        if not level.check_collision(new_rect):
            self.rect.x = new_rect.x
            self.rect.y = new_rect.y
        else:
            # If there's a collision with a wall, stop movement in that direction
            if self.direction.x != 0:
                self.rect.x -= self.direction.x * self.speed * dt
            if self.direction.y != 0:
                self.rect.y -= self.direction.y * self.speed * dt