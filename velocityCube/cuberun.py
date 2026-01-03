import pygame
import random
import time


while True:
    try:
        velocity_input = int(input("please enter your acceleration speed: "))
        break
    except:
        print("enter a number!")
        continue
pygame.init()
width = 1500
height = 800
screen = pygame.display.set_mode((width,height))

running = True



class Box:
    def __init__(self):
        self.x = 0
        self.vx = velocity_input
        self.mass = random.uniform(10, 20)
        self.y = 800 - 30
        self.vy = random.uniform(-300,-500)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.last_time = time.time()
        self.weith = 30
        self.height = 30
        self.hit_wall = False
        self.ballSize = random.uniform(5, 10)
        self.Touchfloor = True
        self.hit_other = True


    
    def velocity_calc(self):

        start_time = time.time()
        dt = start_time - self.last_time
        self.last_time = start_time

        
        self.vx += velocity_input * dt * self.mass
        

        # print(self.vx)
        if self.Touchfloor:
            self.x += self.vx * dt
        
        else:
            self.x -= self.vx *dt
            friction = 1
            self.vx *= friction

            # if abs(self.vx)<5:
            #     self.vx = 0

            
        

        if self.x >= width - self.weith:
            self.x = width - self.weith
            self.hit_wall = True 
            self.vx *= -1.5
        
            self.Touchfloor = False

        if self.x <= 0 - self.weith:
            self.x = 0 + self.weith
            self.vx *= -0.4
            self.hit_other = True
            

            
        if self.y >= height - self.ballSize:
            self.y = height - self.ballSize
            bounce = self.ballSize/20
            bounce = max(0.2, bounce)
            self.vy *= -bounce
            self.vx *= 0.85
            if abs(self.vx) < 5:
                self.vx = 0
            


            
        
        if self.y <= 0 + self.ballSize:
            self.y = self.y + self.ballSize
            bounce = self.ballSize/20
            self.vy *= +bounce

        
        
        if self.hit_wall:
            gravity = 980
            self.vy += gravity * dt
            self.y += self.vy * dt  
        


    def coob(self, screen):
        pygame.draw.rect(screen, self.color,(self.x,self.y, self.weith, self.height))
    
    def circle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.ballSize)


box = Box()
circless = []
for cir in range(10):
    circless.append(Box())


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    
    box.velocity_calc()
    if box.hit_wall == False:
        
        box.coob(screen)
    else:
        for c in circless:
            c.velocity_calc()
            c.circle(screen)
        
    pygame.display.flip()

    