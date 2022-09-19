import pygame
import json

class Player:

    size = 50

    def __init__(self, x, y):

        self.x = 500
        self.y = 500


    def tick(self, handler):

        if handler.getKeyPressed("UP"):
            self.y -= 1

        if handler.getKeyPressed("DOWN"):
            self.y += 1

        if handler.getKeyPressed("LEFT"):
            self.x -= 1

        if handler.getKeyPressed("RIGHT"):
            self.x += 1

    def render(self, display):

        pygame.draw.rect(display, (255,255,0), (self.x, self.y, Player.size, Player.size))

    def prep_msg(self):

        payload = {
            'x' : self.x,
            'y' : self.y
        }

        return json.dumps(payload)
