import pygame as p
import pygame.freetype
from settings import *

p.init()
screen = p.display.set_mode((544, 256))

image = p.image.load("images/tilemap_packed.png")
image = p.transform.scale(image, (544, 256))

font = p.freetype.Font(None, 16)


width = image.get_width()
height = image.get_height()
index = 0
for y in range(0, height, TILE_SIZE):
    for x in range(0, width, TILE_SIZE):
        font.render_to(image, (x + 8, y + 8), f"{index}", (0, 0, 0))
        index += 1

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN
                                    and event.key == p.K_ESCAPE):
            running = False
    screen.blit(image, (0, 0))
    p.display.flip()
