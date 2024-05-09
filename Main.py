import pygame
from sys import exit
from subprocess import call
import random
import button

pygame.init()

def menu():
    pygame.quit()
    call(["python","MENU.py"])
    
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
        for i in range (5):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Attacked/{i}.png').convert_alpha()
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
        for i in range (10):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Dead/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (7):
            img = pygame.image.load(f'Character/{type}/Warrior/{self.name}/Heal/{i}.png').convert_alpha()
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
        screen.blit(self.image, self.image_rect)

class Mage:
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
            img = pygame.image.load(f'Character/{type}/Mage/{self.name}/Idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'Character/{type}/Mage/{self.name}/Attack/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (3):
            img = pygame.image.load(f'Character/{type}/Mage/{self.name}/Attacked/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        for i in range (10):
            img = pygame.image.load(f'Character/{type}/Mage/{self.name}/Dead/{i}.png').convert_alpha()
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
    
    def get_attacked(self):
        self.action = 0
        self.frame_index = 3
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
        screen.blit(self.image, self.image_rect)

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
    
    def draw (self, health):
        self.health = health
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, 'Red', (self.x, self.y, 300, 20))
        pygame.draw.rect(screen, 'Green', (self.x, self.y, 300 * ratio, 20))

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
        
panel_text_group = pygame.sprite.Group()

def show_background():
    upper_background = pygame.image.load('background/upper_background.png').convert_alpha()
    upper_rect = upper_background.get_rect(topleft = (0,0))
    screen.blit(upper_background, upper_rect)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, False, 'Green')
    screen.blit(img, (x, y))

def draw_panel():
    lower_background = pygame.image.load('background/lower_background.png').convert_alpha()
    lower_rect = lower_background.get_rect(topleft = (0,500))
    screen.blit(lower_background, lower_rect)
    draw_text(f'{Player_obj.name} HP: {Player_obj.health}', text_font, 'Green', 100, 510)
    draw_text(f'{Enemy_obj.name} HP: {Enemy_obj.health}', text_font, 'Green', 900, 510)
    draw_text(f'Ramuan tersisa: {Player_obj.potions}', text_font,'Green', 160, 600)

Player_obj = Warrior('Gatot Kaca', 'Player', 100,100, 10, 5, 1)
Enemy_obj = Warrior('Gatot Kaca', 'Enemy', 100,100, 10, 5, 1)

Player_health_bar = HealthBar(100, 550, Player_obj.health, Player_obj.max_health)
Enemy_health_bar = HealthBar(900, 550, Enemy_obj.health, Player_obj.max_health)

potion_button = button.Button(screen, 100, 580, potion_image , 50, 50)
restart_button = button.Button(screen, 300, 10, restart_image, 200, 120)
back_button = button.Button (screen, 700, 10, back_to_menu, 200, 120)

att_sfx = pygame.mixer.Sound(f'Sound/{Player_obj.name}/punch.mp3')
hl_sfx = pygame.mixer.Sound(f'Sound/{Player_obj.name}/heal.mp3')
win_sfx = pygame.mixer.Sound(f'Sound/win.mp3')
lose_sfx = pygame.mixer.Sound(f'Sound/lose.mp3')

while True:

    show_background()
    draw_panel()
    Player_health_bar.draw(Player_obj.health)
    Enemy_health_bar.draw(Enemy_obj.health)
    Player_obj.update()
    Player_obj.draw()
    Enemy_obj.update()
    Enemy_obj.draw()

    panel_text_group.update()
    panel_text_group.draw(screen)
    attack = False
    potion = False
    target = None
    pygame.mouse.set_visible(True)
    mous_pos = pygame.mouse.get_pos()
    if Enemy_obj.image_rect.collidepoint(mous_pos):
        pygame.mouse.set_visible(False)
        screen.blit(sword_image, mous_pos)
        if mous_clicked == True and Enemy_obj.alive == True:
            attack = True
            target = Enemy_obj
    if potion_button.draw():
        potion = True

    if game_over == 0:
        #PLAYER ACTION
        if Player_obj.alive:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and target != None:
                        att_sfx.play()
                        Player_obj.attack_target(Enemy_obj)
                        current_fighter += 1
                        action_cooldown = 0
                    if potion == True:
                        if Player_obj.potions > 0:
                            if Player_obj.max_health - Player_obj.health > 30:
                                heal_amount = 30
                            else:
                                heal_amount = Player_obj.max_health - Player_obj.health
                            hl_sfx.play()
                            Player_obj.healing()
                            Player_obj.health += heal_amount
                            panel_text = Panelinfo(Player_obj.image_rect.centerx, Player_obj.image_rect.y, f'Health + {heal_amount}', 'Green')
                            panel_text_group.add(panel_text)
                            Player_obj.potions -= 1
                            action_cooldown = 0
                            current_fighter += 1
                            potion = False
        else:
            game_over = -1            
        
        #ENEMY ACTION
        if current_fighter == 2:
            if Enemy_obj.alive:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if (Enemy_obj.health / Enemy_obj.max_health) < 0.5 and Enemy_obj.potions > 0:
                        if Enemy_obj.max_health - Enemy_obj.health > 30:
                                heal_amount = 30
                        else:
                            heal_amount = Enemy_obj.max_health - Enemy_obj.health
                        hl_sfx.play()
                        Enemy_obj.healing()
                        Enemy_obj.health += heal_amount
                        panel_text = Panelinfo(Enemy_obj.image_rect.centerx, Enemy_obj.image_rect.y, f'Health + {heal_amount}', 'Green')
                        panel_text_group.add(panel_text)
                        Enemy_obj.potions -= 1
                        current_fighter += 1
                        action_cooldown = 0
                        potion = False
                    else:
                        Enemy_obj.attack_target(Player_obj)
                        att_sfx.play()
                        current_fighter += 1
                        action_cooldown = 0
            else:
                game_over = 1

        #RESET THE TURN
        if current_fighter > total_fighter:
            current_fighter = 1

    if game_over != 0:
        if game_over == 1:
            win_sfx.play()
            screen.blit(win_image, (200,0))
        if game_over == -1:
            lose_sfx.play()
            screen.blit(lose_image, (150,0))
        if restart_button.draw():
            Player_obj.reset()
            Enemy_obj.reset()
            current_fighter = 1
            action_cooldown
            game_over = 0
        if back_button.draw():
            menu()

    #EVENT LOOP
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous_clicked = True
            else:
                mous_clicked = False
    
    
    
    pygame.display.update()
    jam.tick(60)

    
