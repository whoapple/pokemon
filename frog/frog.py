import pygame as p

class Frog(p.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animation = False
        self.frogs = []
        for i in range(1, 11):
            self.frogs.append(p.image.load(f'frog/attack_{i}.png'))
        self.current_sprite = 0
        self.image = self.frogs[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, speed):
        # keys = p.key.get_pressed()
        # if keys[p.K_SPACE]:
        #     self.animation == True
        if self.animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.frogs):
                self.current_sprite = 0
                self.animation = False
        self.image = self.frogs[int(self.current_sprite)]


p.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("frog")
clock = p.time.Clock()

frog = Frog((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

frog_group = p.sprite.GroupSingle()
frog_group.add(frog)

running = True
while running:
    # Выдаёт список всех событий
    for event in p.event.get():
        if event.type == p.KEYDOWN and event.key == p.K_SPACE:
            frog.animation = True
        elif event.type == p.QUIT or event.type == p.KEYDOWN:
            running = False

    screen.fill((0, 0, 0))

    frog_group.draw(screen)
    frog.update(0.25)

    p.display.flip()
    clock.tick(60)
