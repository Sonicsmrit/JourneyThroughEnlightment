# # # import pygame

# # # # pygame setup
# # # pygame.init()
# # # screen = pygame.display.set_mode((1280, 720))
# # # clock = pygame.time.Clock()
# # # running = True

# # # while running:
# # #     # poll for events
# # #     # pygame.QUIT event means the user clicked X to close your window
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # #     # fill the screen with a color to wipe away anything from last frame
# # #     screen.fill("purple")

# # #     # RENDER YOUR GAME HERE

# # #     # flip() the display to put your work on screen
# # #     pygame.display.flip()

# # #     clock.tick(60)  # limits FPS to 60

# # # pygame.quit()

# # # Example file showing a circle moving on screen
# # import pygame

# # # pygame setup
# # pygame.init()
# # screen = pygame.display.set_mode((1280, 720))
# # clock = pygame.time.Clock()
# # running = True
# # dt = 0

# # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# # while running:
# #     # poll for events
# #     # pygame.QUIT event means the user clicked X to close your window
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # fill the screen with a color to wipe away anything from last frame
# #     screen.fill("purple")

# #     pygame.draw.circle(screen, "red", player_pos, 40)

# #     keys = pygame.key.get_pressed()
# #     # if keys[pygame.K_UP]:
# #     #     player_pos.y -= 300 * dt
# #     # if keys[pygame.K_DOWN]:
# #     #     player_pos.y += 300 * dt
# #     # if keys[pygame.K_LEFT]:
# #     #     player_pos.x -= 300 * dt
# #     # if keys[pygame.K_RIGHT]:
# #     #     player_pos.x += 300 * dt

    
# #     # flip() the display to put your work on screen
# #     pygame.display.flip()

# #     # limits FPS to 60
# #     # dt is delta time in seconds since last frame, used for framerate-
# #     # independent physics.
# #     dt = clock.tick(60) / 1000

# # pygame.quit()

# from PIL import Image as img
# import pygame

# with img.open("Test/Furina.jpg") as furina:
    
#     width, height = furina.size
    

#     pixel = []
#     get_position = []
#     step = 5
#     for x in range(0,width, step):
#         for y in range(0,height, step):
#             mango = furina.getpixel((x,y))
#             pixel.append(mango)
#             get_pos = (x,y)
#             get_position.append(get_pos)
    

# pygame.init()

# screen = pygame.display.set_mode((width, height))
# running = True
# print(width,height)

# class pixl():
#     def __init__(self,x,y,color):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.size = 2
    
#     def draw(self, screen):
#         pygame.draw.circle(screen,self.color, (self.x,self.y), self.size)
        

# balls = []

# total = len(pixel)
# for ball in range(total):
#     balls.append(pixl(get_position[ball][0], get_position[ball][1], pixel[ball]))




# while running:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             running = False
        
#     screen.fill("white")
#     for balla in balls:
#         balla.draw(screen)

#     pygame.display.flip()

# pygame.quit()