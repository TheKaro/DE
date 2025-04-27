# src/main.py
import pygame
import settings
from level import Level
from sprites import Pacman, Ghost
from utils import resource_path

def show_menu(screen):
    # Fonts
    title_font = pygame.font.Font(None, 100)  # Bigger font for the title
    prompt_font = pygame.font.Font(None, 74)  # Smaller font for the prompt

    # Text surfaces
    title_text = title_font.render("Diddy's Escape", True, (255, 255, 0))
    prompt_text = prompt_font.render("Press SPACE to Start", True, (255, 255, 0))

    # Get text rectangles
    title_rect = title_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2 - 100))
    prompt_rect = prompt_text.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT // 2))

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        screen.blit(title_text, title_rect)     # Draw title first
        screen.blit(prompt_text, prompt_rect)   # Then draw "Press SPACE to Start"
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def show_game_over(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    text = font.render("You Got Caught!", True, (255, 0, 0))
    subtext = small_font.render("Press any key to exit", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(text, (settings.WIDTH // 2 - text.get_width() // 2, settings.HEIGHT // 2 - text.get_height()))
    screen.blit(subtext, (settings.WIDTH // 2 - subtext.get_width() // 2, settings.HEIGHT // 2 + 20))
    pygame.display.flip()

    # Wait for any key to be pressed
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                waiting = False

    pygame.quit()
    exit()

def main():

    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption('Pac-Man')

    show_menu(screen)

    # Game objects
    level = Level(resource_path('maps/level.txt'))  # Ensure you have a level.txt file
    pacman = Pacman(level.get_center_position())
    ghosts = pygame.sprite.Group(
        Ghost((settings.TILE_SIZE * 9, settings.TILE_SIZE * 7), 'red'),
        Ghost((settings.TILE_SIZE * 10, settings.TILE_SIZE * 7), 'blue'),
        Ghost((settings.TILE_SIZE * 9, settings.TILE_SIZE * 8), 'pink'),
        Ghost((settings.TILE_SIZE * 10, settings.TILE_SIZE * 8), 'orange')
    )
    all_sprites = pygame.sprite.Group(pacman, *ghosts)

    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60) / 1000  # Time per frame in seconds
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.direction = pygame.Vector2(-1, 0)  # Move left
                elif event.key == pygame.K_RIGHT:
                    pacman.direction = pygame.Vector2(1, 0)  # Move right
                elif event.key == pygame.K_UP:
                    pacman.direction = pygame.Vector2(0, -1)  # Move up
                elif event.key == pygame.K_DOWN:
                    pacman.direction = pygame.Vector2(0, 1)  # Move down
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                # Ignore mouse events
                pass

        for ghost in ghosts:
            if pacman.rect.colliderect(ghost.rect):
                show_game_over(screen)

        # Update
        all_sprites.update(dt, level)

        # Draw
        screen.fill(settings.BLACK)
        level.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()