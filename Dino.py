import pygame
import pygame.freetype

class Dino():
    def __init__(self, image, position, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.step = 6
        self.max_jump = 60
        self.in_jump = False
        self.score = 0
        self.game_status = 'Game'
        self.screen = screen

    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y += 1
                self.rect.y -= self.step
            elif self.y < self.max_jump * 2:
                self.y += 1
                self.rect.y += self.step
            else:
                self.in_jump = False
                self.y = False

    def draw(self):
        self.screen.blit(self.image, self.rect)