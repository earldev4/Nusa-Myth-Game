import pygame

class MenuButton():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, text_y_offset=0):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_y_offset = text_y_offset
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos - self.text_y_offset))

    def update(self, display):
        if self.image is not None:
            display.blit(self.image, self.rect)
        display.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class MenuImageButton(MenuButton):
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, size=None, border_color=None, border_width=0):
        super().__init__(image, pos, text_input, font, base_color, hovering_color)
        self.size = size
        if self.size is not None:
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        self.border_color = border_color
        self.border_width = border_width

    def update(self, display):
        # Gambar border
        if self.border_color and self.border_width > 0:
            border_rect = pygame.Rect(self.rect.topleft, self.rect.size)
            pygame.draw.rect(display, self.border_color, border_rect, self.border_width)

        # Gambar gambar tombol
        display.blit(self.image, self.rect)
        display.blit(self.text, self.text_rect)

