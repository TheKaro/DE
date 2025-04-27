import pygame
import os
import settings
import pkgutil
from utils import load_image, resource_path

class Level:
    def __init__(self, map_file: str):
        self.layout = []
        map_path = resource_path('maps/level.txt')
        with open(map_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.layout.append(list(line.rstrip('\n')))

        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.surface = pygame.Surface((self.width, self.height))
        self.walls = []  
        self._load_tiles()
        self._render_maze()
        self._generate_walls()  

    def eat_pellet(self, x: float, y: float) -> str:
        col = int(x) // settings.TILE_SIZE
        row = int(y) // settings.TILE_SIZE
        if self.layout[row][col] in ('.', 'o'):
            pellet = self.layout[row][col]
            self.layout[row][col] = ' '
            return pellet
        return ''

    def _load_tiles(self):
        self.wall_tile = load_image(resource_path('assets/images/wall.png'))
        self.pellet_tile = load_image(resource_path('assets/images/pellet.png'), (settings.TILE_SIZE, settings.TILE_SIZE))  # Scaling here
        self.big_pellet_tile = load_image(resource_path('assets/images/big_pellet.png'), (settings.TILE_SIZE, settings.TILE_SIZE))  # Scaling here

    def _generate_walls(self):
        self.walls = []  

        tile_size = settings.TILE_SIZE
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                if cell == '#':  
                    wall_rect = pygame.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
                    self.walls.append(wall_rect)

    def _render_maze(self) -> None:
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                x = col_index * settings.TILE_SIZE
                y = row_index * settings.TILE_SIZE
                
                if cell == '#':  # Wall
                    self.surface.blit(self.wall_tile, (x, y))
                elif cell == '.':  # Pellet
                    # Scale the normal pellet image
                    pellet_image = pygame.transform.scale(self.pellet_tile, (int(settings.TILE_SIZE * 0.6), int(settings.TILE_SIZE * 0.6)))  
                    self.surface.blit(pellet_image, (x + (settings.TILE_SIZE - pellet_image.get_width()) // 2, y + (settings.TILE_SIZE - pellet_image.get_height()) // 2))
                elif cell == 'o':
                    big_pellet_image = pygame.transform.scale(self.big_pellet_tile, (int(settings.TILE_SIZE * 0.8), int(settings.TILE_SIZE * 0.8))) 

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.surface, (0, 0))

    def is_wall(self, x: float, y: float) -> bool:
        col = int(x) // settings.TILE_SIZE
        row = int(y) // settings.TILE_SIZE
        if 0 <= row < len(self.layout) and 0 <= col < len(self.layout[0]):
            return self.layout[row][col] == '#'
        return False

    def eat_pellet(self, x: float, y: float) -> str:
        col = int(x) // settings.TILE_SIZE
        row = int(y) // settings.TILE_SIZE
        if self.layout[row][col] in ('.', 'o'):
            pellet = self.layout[row][col]
            self.layout[row][col] = ' '  
            return pellet
        return ''
    
    def check_collision(self, new_rect):
        for wall in self.walls:
            if new_rect.colliderect(wall):
                return True  
        return False 
    
    def get_center_position(self) -> tuple:
        rows = len(self.layout)
        cols = len(self.layout[0]) if rows > 0 else 0
        center_x = (cols // 2) * settings.TILE_SIZE + settings.TILE_SIZE // 2
        center_y = (rows // 2) * settings.TILE_SIZE + settings.TILE_SIZE // 2
        return (center_x, center_y)