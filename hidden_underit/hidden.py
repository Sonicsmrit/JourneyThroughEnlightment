import pygame
from PIL import Image as img
import math

with img.open("hidden_underit/smugmiku.jpg") as miku:
    width, height = miku.size
    get_pixl = []
    get_coords = []
    
    step = 4
    for x in range(0,width,step):
        for y in range(0,height,step):
            mango = miku.getpixel((x,y))
            get_pixl.append(mango)
            get_coords.append((x,y))
    

pygame.init()
screen = pygame.display.set_mode((width,height))
running = True
background = pygame.image.load("hidden_underit/miku.jpg").convert()
clock = pygame.time.Clock()

class pic:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y
        self.color = color
        self.size = 10
        self.speed = 50
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size, self.size))


    def mouse_math(self):
        mx, my = pygame.mouse.get_pos()

        dx = self.x - mx
        dy = self.y - my
        dist = math.hypot(dx, dy)

        radius = 100
        strength = 10

        if dist < radius and dist != 0:
            dx /= dist
            dy /= dist

            self.x += dx * strength
            self.y += dy * strength


balls=[]
total = len(get_pixl)
for x in range(total):
    balls.append(pic(get_coords[x][0],get_coords[x][1],get_pixl[x]))


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0,0))

    for ball in balls:
        ball.draw(screen)
        ball.mouse_math()
    
    pygame.display.flip()
    clock.tick(60)
    


