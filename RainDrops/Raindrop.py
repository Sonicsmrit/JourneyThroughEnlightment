import random
import time
import pygame


pygame.init()
screen = pygame.display.set_mode((800,800))

class Drops:

    def __init__(self):
        self.x = random.randint(0,800)
        self.y = -500
        self.speed = random.randint(200,1000)
        self.color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        self.last_time = time.time()
    
    def update(self):
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        self.y += self.speed * dt  #falling of balls

        #position

        #color
        

        # print(self.color)

        if self.y > 800:
            self.y = 0
            self.x = random.randint(0,800)


        # print(self.y)
    
    def circle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), 5)


# while True:
#     fall.update()
#     time.sleep(1)


rain = []
for x in range(100):
    rain.append(Drops())
    

running = True

while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    
    screen.fill('white')
    for drop in rain:
        drop.update()
        drop.circle(screen)
    
    pygame.display.flip()