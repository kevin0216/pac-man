from typing import *
from enum import *

import pygame

from ..core import *
from .config import *

class Environment:

    def __init__(self):
        self.field = Field()
        self.renderer = Renderer()

    @classmethod
    def get_user_input(cls):
        pass

    def update(self):
        self.renderer.render(self.field)


class Renderer:
    """Show the game status to the screen
    """

    def __init__(self):
        
        pygame.init()
        window_size = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
        self.screen = pygame.display.set_mode(window_size)
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def draw_square(self, i: int, j: int, square: Square):

        match square:
            case Square.EMPTY:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (0, 255, 0), rect, 1)
            case _:
                print("???")
    
    def render(self, field: Field):

        self.screen.fill((255, 0, 0))

        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.draw_square(i, j, field.field[i][j])
                        
        pygame.display.update()
        print("OK")
        self.clock.tick(FPS)