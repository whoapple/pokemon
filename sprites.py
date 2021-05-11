import pygame as p


class Player(p.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.image = p.image.load(img)
        self.image = p.transform.scale(self.image, (19*3, 29*3))
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
