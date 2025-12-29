import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
delta_time = 0
player_position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running: 

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    screen.fill("white")

    pygame.draw.circle(screen, "red", player_position, 50)

    if key[pygame.K_UP]:
        player_position.y -= 500*delta_time
    if key[pygame.K_DOWN]:
        player_position.y += 500*delta_time
    if key[pygame.K_LEFT]:
        player_position.x -= 500*delta_time
    if key[pygame.K_RIGHT]:
        player_position.x += 500*delta_time


    

    delta_time = clock.tick(60)/1000
    pygame.display.flip()

pygame.quit()