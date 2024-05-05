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


