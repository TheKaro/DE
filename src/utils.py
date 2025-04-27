# src/utils.py
import os
import pygame
import settings
import sys

# src/utils.py

import pygame
import os
import sys

import os
import sys

def resource_path(relative_path):
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except Exception as e:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def load_image(image_path, size=None):
    """Load an image and optionally scale it."""
    image = pygame.image.load(image_path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image.convert_alpha()

def load_sound(filename: str) -> pygame.mixer.Sound:
    path = os.path.join(os.path.dirname(__file__), os.pardir, settings.SOUND_DIR, filename)
    return pygame.mixer.Sound(path)


def cut_spritesheet(sheet: pygame.Surface, frame_width: int, frame_height: int) -> list:
    frames = []
    for y in range(0, sheet.get_height(), frame_height):
        for x in range(0, sheet.get_width(), frame_width):
            rect = pygame.Rect(x, y, frame_width, frame_height)
            frames.append(sheet.subsurface(rect))
    return frames