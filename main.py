import pygame as p
import sprites as s


p.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = p.time.Clock()

player = s.Player("images/player.png", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
player_group = p.sprite.GroupSingle()
player_group.add(player)

speed = 0

running = True
while running:
    # Выдаёт список всех событий
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill((255, 255, 255))

    player_group.draw(screen)

    p.display.flip()
    clock.tick(60)
