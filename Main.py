import pygame
from sys import exit
import random
import button

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Nusa-Myth')
jam = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
sword_image = pygame.image.load('items/sword.png').convert_alpha()
potion_image = pygame.image.load('Items/potion.png').convert_alpha()
win_image = pygame.image.load('Background/win_background.png').convert_alpha()
lose_image = pygame.image.load('Background/lose_background.png').convert_alpha()
restart_image = pygame.image.load('Items/restart.png')
back_to_menu = pygame.image.load('Items/back.png')

current_fighter = 1
total_fighter = 2
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
mous_clicked = False
game_over = 0

class Warrior:
    def __init__(self,name, type, health, max_health, attack, critical_damage, potions):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.critical_damage = critical_damage
        self.start_potions =potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Attack/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (3):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Attacked/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        for i in range (10):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Dead/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        if self.type == 'Player':
            self.image_rect = self.image.get_rect(midleft = (100, 300))
        else:
            self.image_rect = self.image.get_rect(midleft = (900, 300))
            
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
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    


