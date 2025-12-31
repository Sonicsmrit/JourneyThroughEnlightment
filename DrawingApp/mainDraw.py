import pygame


pygame.init()

def key_color():
    color = {1:'red',2:'black', 3:'green', 4:'blue',5:'yellow'}
    key = pygame.key.get_pressed()
    if key[pygame.K_1]:
        return color[1]
    elif key[pygame.K_2]:
        return color[2]
    elif key[pygame.K_3]:
        return color[3]
    elif key[pygame.K_4]:
        return color[4]
    elif key[pygame.K_5]:
        return color[5]
    else:
        return "white"




screen = pygame.display.set_mode((800,800))
running = True



screen.fill("white")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            color = key_color() #checks if the key was pressed

    

    mouse_xy = pygame.mouse.get_pos()
    mouse_x = mouse_xy[0]
    mouse_y = mouse_xy[1]

    pixl = (mouse_x,mouse_y,20,20) #x,y,size-width, size-height
    
    #preview the colour in hand
    pygame.draw.rect(screen, 'gold', (395, 25, 30, 30))
    try:
        pygame.draw.rect(screen, color,(400, 30, 20,20))
    except:
        pygame.draw.rect(screen, 'white',(400, 30, 20,20))

    #drawing
    mouse_press = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()

    if mouse_press[0]:
        try:
            pygame.draw.rect(screen,color,pixl)
        except:
            pygame.draw.rect(screen,'white',pixl)
    if key[pygame.K_c]:
        screen.fill("white")



    # pygame.draw.rect(screen,'red', pixl)





    pygame.display.flip()

pygame.quit()