import random
from PIL import Image as img
import pygame

with img.open("Particles Recreate Image/makima.jpg") as makima:
    width, height = makima.size

    get_color = []
    get_coords = []
    for x in range(width):
        for y in range(height):
            coords = (x,y)
            get_coords.append(coords)
            mango = makima.getpixel((x,y))
            get_color.append(mango)
    

pygame.init()

screen = pygame.display.set_mode((width,height))
running = True

class ImageCool:
    def __init__(self,color, rx, ry):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.mx = random.randint(0, width)
        self.my = random.randint(0, height)
        self.color = color
        self.Rx = rx
        self.Ry = ry
        self.size = 1

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y),self.size)

    def movement(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.x += (self.Rx - self.x) *0.5
            self.y += (self.Ry - self.y) * 0.5
        
        elif key[pygame.K_r]:
            self.x += (self.mx - self.x) * 0.5
            self.y += (self.my - self.y) * 0.5
            

balls = []

total = len(get_coords)
for x in range(total):
    balls.append(ImageCool(get_color[x], get_coords[x][0], get_coords[x][1]))



while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for ball in balls:
        ball.draw(screen)
        ball.movement()


    pygame.display.flip()

pygame.quit()