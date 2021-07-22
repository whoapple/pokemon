import pygame as p
from settings import *


class BattleScreen():
    def __init__(self, surface, font):
        self.surface = surface
        self.font = font

    def draw(self, message):
        self.font.render_to(self.surface, (SCREEN_WIDTH / 10, SCREEN_HEIGHT / 10), message, (BLACK))
