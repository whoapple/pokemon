import pygame as p


p.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = p.time.Clock()

running = True
while running:
    # Выдаёт список всех событий
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill((255, 0, 0))

    p.display.flip()
    clock.tick(60)
