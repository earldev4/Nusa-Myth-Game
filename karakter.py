import pygame, random
from info import Panelinfo

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Character:
    def __init__(self, name, type, health, max_health, attack, critical_damage, start_potions):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.critical_damage = critical_damage
        self.start_potions = start_potions
        self.potions = start_potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.load_animations()

    def load_animations(self):
        raise NotImplementedError("Subclasses should implement this!")

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack_target(self, target):
        critical = random.randint(0, self.critical_damage)
        damage = self.attack + critical
        target.health -= damage
        target.get_attacked()
        if target.health < 1:
            target.health = 0
            target.alive = False
            target.dead()
        panel_text = Panelinfo(target.image_rect.centerx, target.image_rect.y, f'Damage: {damage}', 'Red')
        panel_text_group.add(panel_text)
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def get_attacked(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def healing(self):
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.health = self.max_health
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.image_rect) # type: ignore

class Warrior(Character):
    def __init__(self, name, type, health, max_health, attack):
        super().__init__(name, type, health, max_health, attack, critical_damage=10, start_potions=1)

    def load_animations(self):
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{self.type}/Warrior/{self.name}/Idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (5):
            img = pygame.image.load(f'Character/{self.type}/Warrior/{self.name}/Attacked/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{self.type}/Warrior/{self.name}/Attack/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (10):
            img = pygame.image.load(f'Character/{self.type}/Warrior/{self.name}/Dead/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (7):
            img = pygame.image.load(f'Character/{self.type}/Warrior/{self.name}/Heal/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        if self.type == 'Player':
            self.image_rect = self.image.get_rect(midleft=(100, 300))
        else:
            self.image_rect = self.image.get_rect(midleft=(900, 300))

class Mage(Character):
    def __init__(self, name, type, health, max_health, attack):
        self.magic = random.randint(0, 10)
        super().__init__(name, type, health, max_health, attack, critical_damage=5, start_potions=2)

    def load_animations(self):
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{self.type}/Mage/{self.name}/Idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (5):
            img = pygame.image.load(f'Character/{self.type}/Mage/{self.name}/Attacked/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{self.type}/Mage/{self.name}/Attack/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (10):
            img = pygame.image.load(f'Character/{self.type}/Mage/{self.name}/Dead/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (7):
            img = pygame.image.load(f'Character/{self.type}/Mage/{self.name}/Heal/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        if self.type == 'Player':
            self.image_rect = self.image.get_rect(midleft=(100, 300))
        else:
            self.image_rect = self.image.get_rect(midleft=(900, 300))

panel_text_group = pygame.sprite.Group()

