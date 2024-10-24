# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(70, 690)
player_size = pygame.Vector2(120,20)
ball_size = pygame.Vector2(20,20)
ball_velocity = 300



def reset_game():
    global ball_pos, ball_direction, score
    score = 0
    ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    

    ball_start_x = 0
    ball_start_y = 0
    while ball_start_x == 0 or ball_start_y == 0:
        ball_start_x = random.randint(-1, 1)
        ball_start_y = random.randint(-1, 1)
    
    ball_direction = pygame.Vector2(ball_start_y, ball_start_x)


reset_game()
player_rect = pygame.Rect((player_pos), (player_size))
ball_rect = pygame.Rect((ball_pos), (ball_size))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    pygame.draw.rect(screen, "black", player_rect) 

    pygame.draw.rect(screen, "black", ball_rect) 

    ball_rect.x -= int(ball_direction.x * ball_velocity * dt)
    ball_rect.y -=  int(ball_direction.y * ball_velocity * dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(300 * dt)
        if player_rect.left <= 0:
            player_rect.left = 0
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(300 * dt)
        if player_rect.right > screen.get_width():
            player_rect.right = screen.get_width()
    if ball_rect.right > screen.get_width() or ball_rect.left < 0:
        ball_direction.x = -ball_direction.x
    if ball_rect.top < 0:
        ball_direction.y = -ball_direction.y
        score += 1
    if player_rect.colliderect(ball_rect):
        ball_direction.y = -ball_direction.y
    if ball_rect.bottom >= screen.get_height():
        print(f"Score: {score}")
        reset_game()
        ball_rect.topleft = (int(ball_pos.x), int(ball_pos.y))  # Reset the ball rectangle position
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
