import pygame as p
import sprites as s
from settings import *

class Game:
    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        p.display.set_caption("player")
        self.clock = p.time.Clock()
        self.running = False

    def new(self):
        self.player_sheet = s.SpriteSheet('images/sheet.png', 4)
        self.all_sprites = p.sprite.LayeredUpdates()
        self.player = s.Player(self, self.player_sheet, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.map = s.Map(self, "map.csv", "images/tilemap_packed.png", 16)
        self.map.load_map()
        self.camera = s.Camera(self.map.width, self.map.height)

    def _events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False

    def _draw(self):
        self.screen.fill(BLACK)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        p.display.flip()

    def _update(self):
        self.player.update()
        self.player.animate()
        self.camera.update(self.player)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self._events()
            self._update()
            self._draw()



if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
