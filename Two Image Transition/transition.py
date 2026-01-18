import pygame
from PIL import Image as img

with img.open("Two Image Transition/frame_00008.jpg") as frame:
    width,height = frame.size

    frame_pixel = []
    gray_frame = frame.convert("L")

    for x in range(width):
        for y in range(height):
            frame_valvs = {
                "color" : frame.getpixel((x,y)),
                "lumin": gray_frame.getpixel((x,y)),
                "coords": ((x,y))
            }
            frame_pixel.append(frame_valvs)


with img.open("Two Image Transition/Miku Hatsune.jpg") as miku:
    miku = miku.resize((width,height))
    gray_miku = miku.convert("L")
    miku_pixel = []
    for x in range(width):
        for y in range(height):
            miku_valvs = {
                "color" : miku.getpixel((x,y)),
                "lumin": gray_miku.getpixel((x,y)),
                "coords": ((x, y))
            }
            miku_pixel.append(miku_valvs)



frame_pixel.sort(key=lambda a:a["lumin"])
miku_pixel.sort(key=lambda a:a["lumin"])

pygame.init()

screen =  pygame.display.set_mode((width,height))
running = True
hold = 300
hold_start = 0
direction = 1
holding = False


time = pygame.time.Clock()

class Transition:
    def __init__(self,x,y,mx,my, color):
        self.x = x
        self.y = y
        self.mx = mx 
        self.my = my
        self.color = color
        self.size = 3
    


    def draw(self, screen):
        pygame.draw.rect(screen, self.color,(int(self.x), int(self.y), self.size, self.size))

    def math(self):
        self.x += (self.mx - self.x) * 0.1
        self.y += (self.my - self.y) * 0.1

    def target(self,mx,my):
        self.mx = mx
        self.my = my
    
    def arrived(self):
        return abs(self.x-self.mx) <0.5 and abs(self.y-self.my)<0.5

rects = []

for i in range(len(miku_pixel)):
    rects.append(Transition(miku_pixel[i]["coords"][0],miku_pixel[i]["coords"][1], frame_pixel[i]["coords"][0],frame_pixel[i]["coords"][1],miku_pixel[i]["color"]))

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False


    arrival_time = True

    screen.fill("white")

    for rect in rects:
        rect.draw(screen)
        
        if not holding:
            rect.math()
        if not rect.arrived():
            arrival_time = False
        
    if arrival_time and not holding:
        holding = True
        hold_start = pygame.time.get_ticks()
    
    if holding:
        if pygame.time.get_ticks() - hold_start >= hold:
            holding = False
            direction *= -1

            for i,rect in enumerate(rects):
                if direction == 1:
                    rect.target(
                        frame_pixel[i]["coords"][0],
                        frame_pixel[i]["coords"][1]
                    )
                else:
                    rect.target(
                        miku_pixel[i]["coords"][0],
                        miku_pixel[i]["coords"][1]
                    )

    pygame.display.flip()

pygame.quit()