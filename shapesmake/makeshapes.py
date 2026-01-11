import pygame
import math
import random

pygame.init()
width, height = (800,800)
screen = pygame.display.set_mode((width,height))
running = True
radius = 50

class shapes:
    def __init__(self, index, total):
        self.x = random.randint(0, width)
        self.y = random.randint(0,height)
        self.index = index
        self.total = total
        self.centerX = width//2
        self.centerY = height//2
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.uniform(10, 15)
        self.tobeX = self.x
        self.tobeY = self.y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.size)

    def math(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_1]:
            #x = centerX + radius * cos(angle)
            #y = centerY + radius * sin(angle)
            
            angle = 2 * math.pi * (self.index/self.total)
            self.tobeX = self.centerX + radius * math.cos(angle)
            self.tobeY = self.centerY + radius * math.sin(angle)

        if key[pygame.K_2]:
            square = 200
            half_sqr = square//2
            per_side = self.total // 4
            pos = self.index%per_side
            side = self.index // per_side
            spacing = square// per_side

            if side == 0: #top
                self.tobeX = self.centerX - half_sqr + pos * spacing
                self.tobeY = self.centerY - half_sqr
            elif side == 1: #right
                self.tobeX = self.centerX + half_sqr
                self.tobeY = self.centerY - half_sqr + pos * spacing
            elif side == 2: #bottom
                self.tobeX = self.centerX + half_sqr - pos * spacing
                self.tobeY = self.centerY + half_sqr
            
            else:  # left
                self.tobeX = self.centerX - half_sqr
                self.tobeY = self.centerY + half_sqr - pos * spacing

        if key[pygame.K_3]:
            per_side = total//3
            side = self.index // per_side
            pos = self.index%per_side
            progress = pos / per_side 

            # Calculate 3 corner points
            tri_height = 150
            top_corner = (self.centerX, self.centerY - tri_height//2)
            bottom_left = (self.centerX - tri_height//2, self.centerY + tri_height//2)
            bottom_right = (self.centerX + tri_height//2, self.centerY + tri_height//2)

            if side == 0:  # Top to bottom-right
                start = top_corner
                end = bottom_right
            elif side == 1:  # Bottom-right to bottom-left
                start = bottom_right
                end = bottom_left
            else:  # side == 2, Bottom-left to top
                start = bottom_left
                end = top_corner

            # Now lerp!
            self.tobeX = start[0] + (end[0] - start[0]) * progress
            self.tobeY = start[1] + (end[1] - start[1]) * progress

        if key[pygame.K_r]:
            self.tobeX = random.randint(0, width)
            self.tobeY = random. randint(0, height)

    def update(self):
        self.x += (self.tobeX -self.x) * 0.01
        self.y += (self.tobeY - self.y) * 0.01










balls = []

total = 200
for x in range(total):
    balls.append(shapes(x, total))



while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    for ball in balls:
        ball.draw(screen)
        ball.math()
        ball.update()

    

    pygame.display.flip()

pygame.quit()