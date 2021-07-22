import random
import pygame as p
from pygame.math import Vector2
import csv
from settings import *


class SpriteSheet:
    def __init__(self, file, animation_len):
        self.sprite_sheet = p.image.load(file).convert_alpha()
        self.animation_len = animation_len
        self.size = Vector2(self.sprite_sheet.get_rect().size)
        sprite_size = self.size / animation_len
        ratio = sprite_size.x / TILE_SIZE
        target_size = self.size / ratio
        self.sprite_size = sprite_size / ratio
        self.sprite_sheet = p.transform.scale(self.sprite_sheet,
                                             (int(target_size.x), int(target_size.y)))
        self.size = Vector2(self.sprite_sheet.get_rect().size)


    def get_image(self, x, y, width, height):
        """Принимает спайтлист"""
        # Вырезаем кусок картинки из спрайтлиста
        image = self.sprite_sheet.subsurface(x, y, width, height)

        return image

class Player(p.sprite.Sprite):
    def __init__(self, game, player_sheet, pos):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        super().__init__(self.groups)

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
        self.rect = self.image.get_rect().inflate(0, -TILE_SIZE*0.5)

        self.rect.center = pos

        self.inventory = {'малое зелье здоровья':0, "покебол":0, 'зелье здоровья':0, 'большое зелье здоровья':0, 'зелье силы':0}
        self.pokemon_list = []
        self.current_pokemon = ''
        self.money = 0


    def update(self):
        """Движение модели"""
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
        self.velocity = self.velocity * PLAYER_SPEED * self.game.dt
        if not self._is_colliding(self.game.walls):
            self.rect.center += self.velocity
        if (self.velocity != Vector2(0, 0)
                            and self._is_colliding(self.game.grass)
                            and random.randint(1, BATTLE_CHANCE) == 1):
            self.game.state = 'BATTLE'
        # self.restrain()

    def _is_colliding(self, group):
        target_rect = self.rect.move(self.velocity)
        for tile in group:
            if target_rect.colliderect(tile.rect):
                return True
        return False

    def restrain(self):
        """Ограничения экрана"""
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def load_images(self):
        """Разделение спрайтлиста на кадры анимации"""
        self.down_walk = []
        self.left_walk = []
        self.right_walk = []
        self.up_walk = []

        w, h = self.player_sheet.sprite_size
        for x in range(0, int(self.player_sheet.size.x), TILE_SIZE):
            self.down_walk.append(self.player_sheet.get_image(x, 0, w, h))
            self.left_walk.append(self.player_sheet.get_image(x, h, w, h))
            self.right_walk.append(self.player_sheet.get_image(x, h*2, w, h))
            self.up_walk.append(self.player_sheet.get_image(x, h*3, w, h))


    def animate(self):
        """Анимирование движения"""
        now = p.time.get_ticks()
        if now - self.last_update > 100 * self.game.dt * FPS:
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


class Map:
    def __init__(self, game, csv_file, tile_map, tile_size, spacing=0):
        self.game = game
        self.csv_file = csv_file
        self.tile_map = tile_map
        self.tile_size = tile_size
        self.spacing = spacing
        self._parse_image()

    def _csv_to_list(self, csv_file):
        """Возвращает 2D список из csv файла."""
        map_list = []
        with open(csv_file) as file:
            data = csv.reader(file)
            for row in data:
                map_list.append(row)
        return map_list

    def _parse_image(self):
        index_to_image_map = {}
        image = p.image.load(self.tile_map)

        if self.tile_size != TILE_SIZE:
            ratio = TILE_SIZE // self.tile_size
            current_size = image.get_rect().size
            # target_size = (current_size[0]*ratio, current_size[1]*ratio)
            target_size = tuple(i * ratio for i in current_size)
            image = p.transform.scale(image, target_size)

        width = image.get_width()
        height = image.get_height()
        index = 0
        for y in range(0, height, TILE_SIZE):
            for x in range(0, width, TILE_SIZE):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                index_to_image_map[index] = tile
                index += 1
        return index_to_image_map

    def _load_tiles(self, map_list, index_to_image_map):
        for i, row in enumerate(map_list):
            for j, index in enumerate(row):
                if int(index) in WALLS:
                    Tile(self.game, j, i, index_to_image_map[int(index)], True)
                elif int(index) in GRASS:
                    Tile(self.game, j, i, index_to_image_map[int(index)], False,
                                                                  is_grass=True)
                else:
                    Tile(self.game, j, i, index_to_image_map[int(index)], False)


    def load_map(self):
        map_list = self._csv_to_list(self.csv_file)
        index_to_image_map = self._parse_image()
        self._load_tiles(map_list, index_to_image_map)
        self.width = len(map_list[0]) * TILE_SIZE
        self.height = len(map_list) * TILE_SIZE


class Tile(p.sprite.Sprite):
    def __init__(self, game, x, y, image, is_wall, is_grass=False):
        self._layer = GROUND_LAYER
        if is_wall:
            self.groups = game.all_sprites, game.walls
        elif is_grass:
            self.groups = game.all_sprites, game.grass
        else:
            self.groups = game.all_sprites
        super().__init__(self.groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Camera:
    def __init__(self, map_width, map_height):
        self.offset = (0, 0)
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, entity):
        return entity.rect.move(self.offset)

    def update(self, target):
        x = -target.rect.x + SCREEN_WIDTH // 2
        y = -target.rect.y + SCREEN_HEIGHT // 2
        x = min(x, 0)
        y = min(y, 0)
        x = max(x, -self.map_width + SCREEN_WIDTH)
        y = max(y, -self.map_height + SCREEN_HEIGHT)
        self.offset = (x, y)
