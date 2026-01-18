import pygame
from PIL import Image as img


with img.open("five transition/all.jpeg") as all_anime:
    width, height = all_anime.size

with img.open("five transition/gojo.jpeg") as gojo_img:
    gojo = gojo_img.resize((width,height))

with img.open("five transition/Isekai.jpeg") as isekai_img:
    isekai = isekai_img.resize((width,height))
    
with img.open("five transition/makima.jpg") as makima_img:
    makima = makima_img.resize((width,height))
    
with img.open("five transition/three.jpeg") as three_img:
    three = three_img.resize((width,height))


index_img = [all_anime, gojo, isekai, makima, three]
pixel = []

for i, image_obj in enumerate(index_img):
    gray_img = index_img[i].convert("L")
    for x in range(width):
        for y in range(height):
            
            pixel_val = {
                "id": i,
                "color": image_obj.getpixel((x,y)),
                "lumin": gray_img.getpixel((x,y)),
                "coords": ((x, y)),
            }
            pixel.append(pixel_val)


pixel.sort(key=lambda a:(a["id"],a["lumin"]))

pygame.init()
##The data teriminal !!##@@~~@@##!!
screen = pygame.display.set_mode((width, height))
running = True
start_hold = 0
hold = 300
holding = False
current_target_index = 1

class Transition:
    def __init__(self,x,y,tx,ty,color):
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        self.size = 12
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen,self.color, (int(self.x), int(self.y), self.size, self.size))

    def target(self,tx,ty):
        self.tx = tx
        self.ty = ty

    def update(self):
        self.x += (self.tx - self.x) *0.1
        self.y += (self.ty - self.y) * 0.1
    
    def arrived(self):
        return abs(self.x-self.tx) <0.5 and abs(self.y-self.ty)<0.5



particles = []
pixels_per_image = width * height

for i in range(0, len(pixel), 10):

    if pixel[i]["id"] == 0:

        next_pixel_index = i + pixels_per_image # jumps to the next image
        target_pixel = pixel[next_pixel_index]
        
        # 2. Extract target coordinates (tx, ty)
        tx = target_pixel["coords"][0]
        ty = target_pixel["coords"][1]

        particles.append(Transition(pixel[i]["coords"][0],
                                    pixel[i]["coords"][1],
                                    tx,
                                    ty,
                                    pixel[i]["color"]))

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    arrival = True

    

    screen.fill("white")
    for particle in particles:

        particle.draw(screen)

        if not holding:
            particle.update()
        
        if not particle.arrived():
            arrival = False
    
    if arrival and not holding:
        holding = True
        start_hold = pygame.time.get_ticks()
    
    if holding:
        if pygame.time.get_ticks() - start_hold >= hold:
            holding = False
            
            current_target_index = (current_target_index + 1) % len(index_img)

            base = current_target_index * pixels_per_image

            for i, particle in enumerate(particles):
                target_pixel = pixel[base + i * 10]
                particle.target(
                    target_pixel["coords"][0],
                    target_pixel["coords"][1]
                )
                





    pygame.display.flip()