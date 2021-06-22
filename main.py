import pygame as p
import sprites as s
from settings import *


p.init()
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("player")
clock = p.time.Clock()

player_sheet = s.SpriteSheet('images/sheet.png', 4)
player = s.Player(player_sheet, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
player_group = p.sprite.GroupSingle()
player_group.add(player)

tile_group = p.sprite.Group()
map = s.Map(tile_group, "map.csv", "images/tilemap_packed.png", 16)
map.load_map()


running = True
while running:
    # Выдаёт список всех событий
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    # for event in p.event.get():
    #     if event.type == p.KEYDOWN and event.key == p.K_d:
    #         player.animation = Truehttps://www.youtube.com/watch?v=DGN0Dk1Q26U
    #     elif event.type == p.QUIT or event.type == p.KEYDOWN:
    #         running = False

    screen.fill(BLACK)

    tile_group.draw(screen)
    player_group.draw(screen)
    # player.run(0.1)
    player.update()
    player.animate()


    p.display.flip()
    clock.tick(60)
