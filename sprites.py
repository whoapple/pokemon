import pygame as p


class Player(p.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.image = p.image.load(img)
        self.image = p.transform.scale(self.image, (50*2, 37*2))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.inventory = {'малое зелье здоровья':0, "покебол":0, 'зелье здоровья':0, 'большое зелье здоровья':0, 'зелье силы':0}
        self.pokemon_list = []
        self.current_pokemon = ''
        self.money = 0

    def update(self):
    
