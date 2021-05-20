import pygame as p



class SpriteSheet:
    def __init__(self, file):
        self.sprite_sheet = p.image.load(file)

    def get_image(self, x, y, width, height):
        # Вырезаем кусок картинки из спрайтлиста
        image = p.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image


player_sheet = SpriteSheet('images/sheet.png')


class Player(p.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.animation = False
        self.players = []
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
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.rect.y -= 5
        if keys[p.K_s]:
            self.rect.y += 5
        if keys[p.K_a]:
            self.rect.x -= 5
        if keys[p.K_d]:
            self.rect.x += 5
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
        while y <= 128:
            
            x += 32

    # def running(self, speed):
    #     # keys = p.key.get_pressed()
    #     # if keys[p.K_SPACE]:
    #     #     self.animation == True
    #     if self.animation == True:
    #         self.current_sprite += speed
    #         if int(self.current_sprite) >= len(self.players):
    #             self.current_sprite = 0
    #             self.animation = False
    #     self.image = self.players[int(self.current_sprite)]
