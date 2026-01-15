import pygame
from PIL import Image as img

with img.open("firsttosecond/makima.jpg") as makima:
    width_makima, height_makima = makima.size

    get_makima_pixels = []
    gray_makima = makima.convert("L")


    for x in range(width_makima):
        for y in range(height_makima):
            get_makima_pixels.append({
                "color": makima.getpixel((x,y)),
                "lumin":gray_makima.getpixel((x,y)),
                "pos": ((x,y))
            })


with img.open("firsttosecond/seen.jpg") as seen:
    seen = seen.resize((width_makima,height_makima))

    get_seen_pixels = []
    gray_seen = seen.convert("L")


    for x in range(width_makima):
        for y in range(height_makima):
            get_seen_pixels.append(
                {
                    "color": seen.getpixel((x,y)),
                    "lumin": gray_seen.getpixel((x,y)),
                    "pos":((x,y))
                    
                }
            )

get_makima_pixels.sort(key=lambda p: p["lumin"])
get_seen_pixels.sort(key=lambda p: p["lumin"])




pygame.init()
width, height = (width_makima,height_makima)
screen = pygame.display.set_mode((width,height))
running = True

class Transaction:
    def __init__(self,x,y,color,mx,my):
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        self.size = 1
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
    
    def math(self):
        self.x += (self.mx - self.x) * 0.1
        self.y += (self.my - self.y) * 0.1



particles= []


total = len(get_makima_pixels)
print(total)
for i in range(total):
    particles.append(Transaction(get_makima_pixels[i]["pos"][0],get_makima_pixels[i]["pos"][1],get_makima_pixels[i]["color"], get_seen_pixels[i]["pos"][0],get_seen_pixels[i]["pos"][1]))


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    


    screen.fill("white")
    for particle in particles:
        particle.draw(screen)
        particle.math()

    pygame.display.flip()

pygame.quit()


#Alogrithm
# The program first sorts both images pixel dictionaries by luminance.
# This changes the order of pixels in the lists but does not change their actual (x, y) positions.

# When particles are created, each particle starts at its original Makima pixel position, so the first image appears unchanged.

# Each particle is also assigned a target position taken from the Seen image at the same brightness rank.

# During the animation, particles simply move from their start position to that target position.

# Because dark pixels were paired with dark pixels and bright pixels with bright pixels, the second image forms correctly.