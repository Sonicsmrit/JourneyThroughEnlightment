import pygame
import random
import math
import time

pygame.init()
width, height = (800, 800)
screen = pygame.display.set_mode((width,height))
running = True

#v = u + at; f= ma; a = f/m; m=10, ke = 1/2 mv^2 


class Balls:
    def __init__(self):
        self.y = 0
        self.x = random.randint(0, width)
        self.distance = None
        self.vy = 0
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.uniform(10,18)
        self.vx = 0
        self.last_time = time.time()
        

    def update(self):
        start_time = time.time()
        gravity = 100
        
        
        dt = start_time - self.last_time
        
        self.vy += gravity*dt *self.size #a = gt

        self.last_time = start_time
        self.y += self.vy * dt #v = u + at; a = gt

        
        self.x += self.vx * dt
        


        if self.y >= 800-self.size:

            # KE = 0.5 * self.mass * self.speed ** 2
            # acceleration = gravity
            
            # force = acceleration*self.mass

            # self.y -= KE/force
            # THis formula just calc the distance dute to which  it teleported to that distance, thats why i introduced velocity

            

            self.y = height - self.size
            bounce = (self.size/20) +0.1
            bounce = max(0.3,bounce)
            self.vy *= -bounce
            self.vx *= -0.5
            self.vx += random.uniform(-100, 100) 
        
        if self.x >= 800-self.size:
            self.x = width - self.size
            self.vx -= 500
        if self.x <= 0 + self.size:
            self.x = 0 + self.size
            self.vx += 500




    
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
            






balls = []
for i in range(100):
    balls.append(Balls())



while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    
    screen.fill('white')
    for ball in balls:
        ball.update()
        ball.draw(screen)

    
    pygame.display.flip()

pygame.quit()