import pygame

pygame.init()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

class Panelinfo(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = text_font.render(damage, False, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 30:
            self.kill()