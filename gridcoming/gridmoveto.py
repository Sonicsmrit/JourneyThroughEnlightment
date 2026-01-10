import pygame
import random

pygame.init()
width,height = (800, 800)
screen = pygame.display.set_mode((width,height))
running = True

class particles:
    def __init__(self, index, total):
        self.x = random.randint(0,width)
        self.y = random.randint(0, height)
        self.size= random.uniform(10,15)
        self.tx = self.x
        self.ty = self.y
        
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.index = index
        self.total = total

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y),self.size)

    def util(self):
        key = pygame.key.get_pressed()
        new_pos_x =  width//2
        new_pos_y = height//2
        square = 200
        half_sqr = square/2
        

        if key[pygame.K_SPACE]:
            per_side = self.total//4
            side = self.index// per_side #it chooses the side of the square the balll will be on
            pos = self.index%per_side ##This tells where the position of the ball on the side is ex: index 15%15 = 0 so it will be the first ball on that side
            spacing = square //per_side  #spacing between balls

            if side == 0: #top
                self.tx = new_pos_x - half_sqr + pos * spacing
                self.ty = new_pos_y - half_sqr
            elif side == 1: #right
                self.tx = new_pos_x + half_sqr
                self.ty = new_pos_y - half_sqr + pos * spacing
            elif side == 2: #bottom
                self.tx = new_pos_x + half_sqr - pos * spacing
                self.ty = new_pos_y + half_sqr
            
            else:  # left
                self.tx = new_pos_x - half_sqr
                self.ty = new_pos_y + half_sqr - pos * spacing

            self.x += (self.tx-self.x) * 0.01 #lerp
            self.y += (self.ty-self.y) * 0.01

        if key[pygame.K_r]:
            self.x = random.randint(0,width)
            self.y = random.randint(0, height)

            




parts = []
total = 200
for x in range(total):
    parts.append(particles(x, total))


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    screen.fill("white")


    for part in parts:
        part.draw(screen)
        part.util()


    pygame.display.flip()