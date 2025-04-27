# src/settings.py
import pygame

# Window dimensions
# Window dimensions
WIDTH = 1920
HEIGHT = 1080
TILE_SIZE = 24  # You can adjust this later if needed
MAZE_WIDTH = WIDTH // TILE_SIZE
MAZE_HEIGHT = HEIGHT // TILE_SIZE

# Speeds (pixels per second)
PACMAN_SPEED = 100
GHOST_SPEED = 80

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Asset directories
IMAGE_DIR = "../assets/images"
SOUND_DIR = "../assets/sounds"