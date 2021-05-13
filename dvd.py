import pygame as p


class DVD(p.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.image = p.image.load(img)
        self.image = p.transform.scale(self.image, (1589//10, 827//10))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.speed_x = 5
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.left <= 0:
            self.speed_x *= -1


p.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("dvd")


clock = p.time.Clock()

dvd = DVD("images/dvd.png", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
dvd_group = p.sprite.GroupSingle()
dvd_group.add(dvd)

speed = 0

running = True
while running:
    # Выдаёт список всех событий
    for event in p.event.get():
        if event.type == p.QUIT or event.type == p.KEYDOWN:
            running = False

    screen.fill((0, 0, 0))

    dvd_group.draw(screen)
    dvd.update()


    p.display.flip()
    clock.tick(60)
