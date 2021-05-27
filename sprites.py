import pygame as p
from pygame.math import Vector2


class SpriteSheet:
    def __init__(self, file):
        self.sprite_sheet = p.image.load(file)
        self.sprite_sheet = p.transform.scale(self.sprite_sheet, (256, 256))

    def get_image(self, x, y, width, height):
        # Вырезаем кусок картинки из спрайтлиста
        image = p.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

class Player(p.sprite.Sprite):
    def __init__(self, player_sheet, pos):
        super().__init__()

        self.player_sheet = player_sheet
        self.animation = False
        self.last_update = 0
        self.frame = 0
        self.players = []
        self.load_images()
        self.animation_cycle = self.up_walk
        # for i in range(1, 7):
        #     self.players.append(p.image.load(f'images/player_{i}.png'))
        # self.current_sprite = 0
        self.image = player_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.inventory = {'малое зелье здоровья':0, "покебол":0, 'зелье здоровья':0, 'большое зелье здоровья':0, 'зелье силы':0}
        self.pokemon_list = []
        self.current_pokemon = ''
        self.money = 0


    def update(self):
        # Выдаёт словарь {K_w: True}
        self.velocity = Vector2(0, 0)
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.velocity.y = -1
        elif keys[p.K_s]:
            self.velocity.y = 1
        elif keys[p.K_a]:
            self.velocity.x = -1
        elif keys[p.K_d]:
            self.velocity.x = 1
        self.rect.center += self.velocity * 5
        self.restrain()

    def restrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def load_images(self):
        self.down_walk = []
        self.left_walk = []
        self.right_walk = []
        self.up_walk = []
        x = 0
        y = 0
        width = 64
        height = 64
        for x in range(0, 192, 64):
            self.down_walk.append(self.player_sheet.get_image(x, 0, width, height))
            self.left_walk.append(self.player_sheet.get_image(x, 64, width, height))
            self.right_walk.append(self.player_sheet.get_image(x, 128, width, height))
            self.up_walk.append(self.player_sheet.get_image(x, 192, width, height))

    # def run(self, speed):
    #     # keys = p.key.get_pressed()
    #     # if keys[p.K_SPACE]:
    #     #     self.animation == True
    #     if self.animation == True:
    #         self.current_sprite += speed
    #         if int(self.current_sprite) >= len(self.players):
    #             self.current_sprite = 0
    #             self.animation = False
    #     self.image = self.players[int(self.current_sprite)]

    def animate(self):
        now = p.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now

            if self.velocity == Vector2(0,0):
                self.frame = -1
            if self.velocity.x < 0:
                self.animation_cycle = self.left_walk
            if self.velocity.x > 0:
                self.animation_cycle = self.right_walk
            if self.velocity.y < 0:
                self.animation_cycle = self.up_walk
            if self.velocity.y > 0:
                self.animation_cycle = self.down_walk
            self.frame = (self.frame + 1) % len(self.animation_cycle)
            self.image = self.animation_cycle[self.frame]
