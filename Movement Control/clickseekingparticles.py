import pygame
import random

pygame.init()
weith, height = (800, 800)
screen = pygame.display.set_mode((weith,height))
running = True

#new_pos = current + (target - current) * progress

class objects:
    def __init__(self):
        self.x = random.randint(0, weith)
        self.y = random.randint(0, height)
        self.vx = 0
        self.vy = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.uniform(5,15)
        self.mx = self.x
        self.my = self.y

    def math(self):
        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0]:
            self.mx, self.my = pygame.mouse.get_pos()
            self.x = self.x + (self.mx - self.x) * 0.02
            self.y = self.y + (self.my - self.y) * 0.02
        
        
        if mouse_click[2]:
            self.x = random.randint(0, weith) 
            self.y = random.randint(0, height)

            
        




    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.size)


circles = []

for i in range(50):
    circles.append(objects())

while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for circle in circles:
        circle.draw(screen)
        circle.math()


    pygame.display.flip()

pygame.quit()