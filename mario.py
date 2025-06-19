import pygame
import sys
import os

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
PLAYER_WIDTH = 50  # Desired width for the player
PLAYER_HEIGHT = 50  # Desired height for the player
OBSTACLE_WIDTH = 30  # Width for the obstacle (Goomba)
OBSTACLE_HEIGHT = 30  # Height for the obstacle (Goomba)
GRAVITY = 1
JUMP_STRENGTH = 15
GOOMBA_SPEED = 1  # Reduced speed for Goombas

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self, screen_height):
        # Position the player at the very bottom of the screen
        self.rect = pygame.Rect(100, screen_height - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity_y = 0
        self.is_jumping = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -JUMP_STRENGTH

        # Apply gravity
        if self.is_jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += GRAVITY  # Gravity pulls the player down

            # Check if the player has landed
            if self.rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:  # Reset position if on the ground
                self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
                self.is_jumping = False
                self.velocity_y = 0  # Reset vertical velocity

        # Ensure the player doesn't go above the screen
        if self.rect.y < 0:
            self.rect.y = 0
            self.velocity_y = 0

# Obstacle class
class Obstacle:
    def __init__(self, x, screen_height):
        # Position the Goombas at the very bottom of the screen
        self.rect = pygame.Rect(x, screen_height - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def move(self, player_x):
        # Simple decision-making to simulate neural network behavior
        if player_x < self.rect.x and self.rect.x > 0:  # Move left if player is to the left
            self.rect.x -= GOOMBA_SPEED  # Reduced speed
        elif player_x > self.rect.x and self.rect.x < SCREEN_WIDTH - OBSTACLE_WIDTH:  # Move right if player is to the right
            self.rect.x += GOOMBA_SPEED  # Reduced speed

# Main game loop
def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 74)  # Font for game over text

    # Load Images with transparency
    goomba_path = resource_path('goomba.png')
    mario_path = resource_path('mario.png')
    wallpaper_path = resource_path('wallpaper.jpg')
    player_image = pygame.image.load(mario_path).convert_alpha()  # Changed to mario.png
    obstacle_image = pygame.image.load(goomba_path).convert_alpha()  # Ensure this file exists
    background_image = pygame.image.load(wallpaper_path).convert()  # Load your background image

    # Get the actual screen size
    screen_width, screen_height = pygame.display.get_surface().get_size()

    # Scale the background image to fit the screen
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Resize Images
    player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    def reset_game():
        player.rect.x = 100
        player.rect.y = screen_height - PLAYER_HEIGHT  # Adjusted for new position
        player.velocity_y = 0
        player.is_jumping = False
        # Spread out 3 Goombas more (twice as far apart)
        return [Obstacle(i * (screen_width // 3) + 300, screen_height) for i in range(3)]  # Adjusted spacing

    player = Player(screen_height)
    obstacles = reset_game()

    camera_x = 0
    running = True
    game_over = False

    while running:
        # Draw the background
        screen.blit(background_image, (0, 0))

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                game_over = False
                obstacles = reset_game()  # Restart the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Exit the game on Escape key
                    running = False

        if not game_over:
            player.move(keys)

            # Camera follows the player
            camera_x = player.rect.x - screen_width // 2 + PLAYER_WIDTH // 2
            if camera_x < 0:
                camera_x = 0

            # Draw player
            screen.blit(player_image, (player.rect.x - camera_x, player.rect.y))

            # Draw obstacles and check for collisions
            for obstacle in obstacles:
                obstacle.move(player.rect.x)  # Move Goombas based on player position
                screen.blit(obstacle_image, (obstacle.rect.x - camera_x, obstacle.rect.y))
                if player.rect.colliderect(obstacle.rect):
                    game_over = True  # Set game over flag

            pygame.display.flip()
            clock.tick(60)
        else:
            # Display Game Over text
            game_over_text = font.render("Game Over", True, RED)
            text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(game_over_text, text_rect)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()