import multiprocessing

import pygame as p
import pygame.freetype

import sprites as s
from settings import *
from battle_screen import BattleScreen
import pokemon as pk


class Game:
    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = p.time.Clock()
        self.running = False
        self.state = 'RPG'
        self.fighting = False

    def new(self):
        self.battle_process =  multiprocessing.Process(target=pk.run)
        self.player_sheet = s.SpriteSheet('images/sheet.png', 4)
        main_font = p.freetype.Font(None, 32)
        self.battle_screen = BattleScreen(self.screen, main_font)
        self.all_sprites = p.sprite.LayeredUpdates()
        self.walls = p.sprite.Group()
        self.grass = p.sprite.Group()
        self.player = s.Player(self, self.player_sheet, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.map = s.Map(self, "map.csv", "images/tilemap_packed.png", 16)
        self.map.load_map()
        self.camera = s.Camera(self.map.width, self.map.height)

    def _events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False

    def _draw(self):
        if self.state == 'RPG':
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.state == 'BATTLE':
            self.screen.fill(WHITE)
            self.battle_screen.draw('Покемоны вселились в твою консоль!!!')
            if not self.fighting:
                self.battle_process.start()
                self.fighting = True

            # self.battle_screen.shop()
        p.display.set_caption(f"{int(self.clock.get_fps())}")
        p.display.flip()


    def _update(self):
        if self.state == 'RPG':
            self.player.update()
            self.player.animate()
            self.camera.update(self.player)
        if self.state == 'BATTLE':
            if not self.battle_process.is_alive:
                self.state == 'RPG'

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self._events()
            self._update()
            self._draw()


if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
