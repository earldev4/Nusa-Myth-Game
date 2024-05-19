import pygame, sys, random, button
from sys import exit
from menu_button import MenuButton, MenuImageButton
from musik import Music
from info import Panelinfo
from karakter import Warrior, Mage 

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

      
panel_text_group = pygame.sprite.Group()

upper_background = pygame.image.load('Background/upper_background.png').convert_alpha()

class PilihArena:
    def __init__(self, arena):
        global upper_background
        self.arena = arena
        self.show_background()

    def show_background(self):
        global upper_background  # Deklarasikan variabel global
        upper_background = pygame.image.load(self.arena).convert_alpha()
        upper_rect = upper_background.get_rect(topleft=(0, 0))
        screen.blit(upper_background, upper_rect)
        # pygame.display.flip()  # Perbarui layar

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

selected_arena = 'Background/upper_background.png'
list_arena = {'Background/upper_background.png': "Candi",
             'Background/Pelabuhan.png': "Pelabuhan",
             'Background/Hutan.png': "Hutan"}

key_pilihan_arena = selected_arena
value_pilihan = list_arena[key_pilihan_arena]

selected_hero = 'a'
list_hero = {'a': Warrior('Bandung Bondowoso', 'Player', 100, 100, 10),
             'b': Warrior('Garuda', 'Player', 100, 100, 10),
             'c': Warrior('Gatot Kaca', 'Player', 100, 100, 10),
             'd': Mage('Banaspati', 'Player', 100, 100, 10),
             'e': Mage('Nyi Roro Kidul', 'Player', 100, 100, 10),
             'f': Mage('Samsudin', 'Player', 100, 100, 10)}

key_pilihan = selected_hero
value_pilihan = list_hero[key_pilihan]

Player_obj = Warrior('Bandung Bondowoso', 'Player', 100, 100, 10)

Enemy_obj = Warrior('Bandung Bondowoso', 'Enemy', 100, 100, 10)

class RandomHeroMusuh:
    def __init__ (self):
        global Enemy_obj 
        self.jenis = [Warrior, Mage]
        self.tipe_warrior = ['Bandung Bondowoso', 'Garuda', 'Gatot Kaca']
        self.tipe_mage = ['Banaspati', 'Nyi Roro Kidul']
        self.role = random.choice(self.jenis)

        if self.role == Warrior:
            self.pilihan = random.choice(self.tipe_warrior)
        if self.role == Mage:
            self.pilihan = random.choice(self.tipe_mage)

        Enemy_obj = self.role(self.pilihan, 'Enemy', 100, 100, 10)

#  Punyaku 
class PilihHero:
    def __init__(self, role, pilihan):
        global Player_obj
        self.role = role
        self.pilihan = pilihan

        Player_obj = self.role(self.pilihan, 'Player', 100, 100, 100)

Player_health_bar = HealthBar(100, 550, Player_obj.health, Player_obj.max_health)
Enemy_health_bar = HealthBar(900, 550, Enemy_obj.health, Player_obj.max_health)

potion_button = button.Button(screen, 100, 580, potion_image , 50, 50)
restart_button = button.Button(screen, 300, 10, restart_image, 200, 120)
back_button = button.Button (screen, 700, 10, back_to_menu, 200, 120)

patt_sfx = pygame.mixer.Sound(f'Sound/{Player_obj.name}/punch.mp3')
phl_sfx = pygame.mixer.Sound(f'Sound/{Player_obj.name}/heal.mp3')
eatt_sfx = pygame.mixer.Sound(f'Sound/{Enemy_obj.name}/punch.mp3')
ehl_sfx = pygame.mixer.Sound(f'Sound/{Enemy_obj.name}/heal.mp3')
win_sfx = pygame.mixer.Sound(f'Sound/win.mp3')
lose_sfx = pygame.mixer.Sound(f'Sound/lose.mp3')

SFX = pygame.mixer.Sound("MAIN MENU/background_music/SFX angklung.mp3")
BACKGROUND = pygame.image.load("MAIN MENU/background/Brick_Background.png")

# obj dari class music, di awal di set lagu menu, nti di sebelum start di ganti lagunya pake method change
BGM = Music()
BGM.load_music('MAIN MENU/background_music/BGM sunda.mp3')
BGM.play_music(-1)
bgm_playing = True
bgm_battle = 'a'

def get_font(size):
    return pygame.font.Font("MAIN MENU/menu_font/font2.ttf", size)
def get_credit_font(size):
    return pygame.font.Font("MAIN MENU/menu_font/font1.ttf", size)

def options():
    global bgm_playing 
    SFX.play()
    while True:
        POSISI_MOUSE = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0, 0))


        OPTIONS_BACK = MenuButton(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color=(23,161,117))

        OPTIONS_BACK.changeColor(POSISI_MOUSE)
        OPTIONS_BACK.update(screen)

        bgm_button_text = "Turn Music Off" if bgm_playing else "Turn Music On"
        BGM_BUTTON = MenuButton(image=None, pos=(640, 360), 
                            text_input=bgm_button_text, font=get_font(40), base_color="White", hovering_color=(23,161,117))

        BGM_BUTTON.changeColor(POSISI_MOUSE)
        BGM_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(POSISI_MOUSE):
                    SFX.play()
                    main_menu()

                if BGM_BUTTON.checkForInput(POSISI_MOUSE):
                    bgm_playing = not bgm_playing
                    if not bgm_playing:
                        SFX.play()
                        BGM.pause_music()
                    else:
                        SFX.play()
                        BGM.unpause_music()

        pygame.display.update()

def credit():
    SFX.play()
    while True:
        CREDIT_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0, 0))

        credits = [
            "Credits",
            "GAME INI DIBUAT OLEH ",
            "Arkan Hariz",
            "Bagas Andreanto",
            "Deva Ahmad",
            "Dzaki Gastia",
            "Fadil Alfitra",
            "Fawwaz Abhitah",
            "Music by DJ Sunda"
        ]
        y_offset = 100
        for line in credits:
            credit_text = get_credit_font(30).render(line, True, "White")
            credit_rect = credit_text.get_rect(center=(640, y_offset))
            screen.blit(credit_text, credit_rect)
            y_offset += 50

        CREDIT_BACK = MenuButton(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_credit_font(40), base_color="White", hovering_color=(23,161,117))

        CREDIT_BACK.changeColor(CREDIT_MOUSE_POS)
        CREDIT_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDIT_BACK.checkForInput(CREDIT_MOUSE_POS):
                    SFX.play()
                    main_menu()

        pygame.display.update()

def main_menu():

    while True:
        screen.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        main_menu_title = pygame.image.load("MAIN MENU/object/Nusa Myth.png")
        MENU_RECT = main_menu_title.get_rect(center=(640, 100))
        
        PLAY_BUTTON = MenuButton(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 275), 
                            text_input="PLAY", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)
        OPTIONS_BUTTON = MenuButton(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 400), 
                            text_input="SETTINGS", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)
        CREDIT_BUTTON = MenuButton(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 525), 
                            text_input="CREDIT", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)

        QUIT_BUTTON = MenuButton(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 650), 
                            text_input="QUIT", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)

        screen.blit(main_menu_title, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, CREDIT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def select_hero(hero):
    global selected_hero
    selected_hero = hero

def play():
    SFX.play()
    while True:
        POSISI_MOUSE = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0, 0))

        WARRIOR_Button = MenuButton(image=None, pos=(340, 70), 
                            text_input="WARRIOR", font=get_font(75), base_color="White", hovering_color=(23,161,117))
        hero1 = MenuButton(image=None, pos=(340, 200), 
                            text_input="Bandung Bondowoso", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        hero2 = MenuButton(image=None, pos=(340, 280), 
                            text_input="Garuda", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        hero3 = MenuButton(image=None, pos=(340, 360), 
                            text_input="Gatot Kaca", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        
        MAGE_Button = MenuButton(image=None, pos=(940, 70), 
                            text_input="MAGE", font=get_font(75), base_color="White", hovering_color=(23,161,117))
        hero4 = MenuButton(image=None, pos=(940, 200), 
                            text_input="Banaspati", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        hero5 = MenuButton(image=None, pos=(940, 280), 
                            text_input="Nyi Roro Kidul", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        hero6 = MenuButton(image=None, pos=(940, 360), 
                            text_input="Samsudin", font=get_font(50), base_color="White", hovering_color=(23,161,117))
        
        BACK_Button = MenuButton(image=None, pos=(340, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color=(23,161,117))
        CONTINUE_Button = MenuButton(image=None, pos=(940, 660), 
                            text_input="CONTINUE", font=get_font(75), base_color="White", hovering_color=(23,161,117))

        BACK_Button.changeColor(POSISI_MOUSE)
        CONTINUE_Button.changeColor(POSISI_MOUSE)
        hero1.changeColor(POSISI_MOUSE)
        hero2.changeColor(POSISI_MOUSE)
        hero3.changeColor(POSISI_MOUSE)
        hero4.changeColor(POSISI_MOUSE)
        hero5.changeColor(POSISI_MOUSE)
        hero6.changeColor(POSISI_MOUSE)

        BACK_Button.update(screen)
        CONTINUE_Button.update(screen)
        hero1.update(screen)
        hero2.update(screen)
        hero3.update(screen)
        hero4.update(screen)
        hero5.update(screen)
        hero6.update(screen)
        MAGE_Button.update(screen)
        WARRIOR_Button.update(screen)

        selected_hero_name = list_hero[selected_hero].name if selected_hero else "No Hero Selected"
        selected_hero_text = "Selected Hero: " + selected_hero_name

        selected_hero_button = MenuButton(image=None, pos=(640, 550),text_input=selected_hero_text, font=get_font(40), base_color="White", hovering_color=(23,161,117))
        selected_hero_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_Button.checkForInput(POSISI_MOUSE):
                    SFX.play()
                    main_menu()
                if CONTINUE_Button.checkForInput(POSISI_MOUSE):
                    SFX.play()
                    RandomHeroMusuh()
                    pilih_arena()
                if hero1.checkForInput(POSISI_MOUSE):
                    PilihHero(Warrior, 'Bandung Bondowoso')
                    select_hero('a')
                if hero2.checkForInput(POSISI_MOUSE):
                    PilihHero(Warrior, 'Garuda')
                    select_hero('b')
                if hero3.checkForInput(POSISI_MOUSE):
                    PilihHero(Warrior, 'Gatot Kaca')
                    select_hero('c')
                if hero4.checkForInput(POSISI_MOUSE):
                    PilihHero(Mage, 'Banaspati')
                    select_hero('d')
                if hero5.checkForInput(POSISI_MOUSE):
                    PilihHero(Mage, 'Nyi Roro Kidul')
                    select_hero('e')
                if hero6.checkForInput(POSISI_MOUSE):
                    PilihHero(Mage, 'Samsudin')
                    select_hero('f')
                
        pygame.display.update()

def select_arena(arena):
    global selected_arena
    selected_arena = arena

def pilih_arena():
    SFX.play()
    while True:
        POSISI_MOUSE = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0, 0))

        button_candi = pygame.image.load('Background/upper_background.png')
        button_candi_size = (300, 200)
        menu_button_candi = MenuImageButton(button_candi, (300, 370), None, pygame.font.Font(None, 36), (255, 255, 255), (23, 161, 117), button_candi_size)
        
        button_pelabuhan = pygame.image.load('Background/Pelabuhan.png')
        button_pelabuhan_size = (300, 200)
        menu_button_pelabuhan = MenuImageButton(button_pelabuhan, (640, 370), None, pygame.font.Font(None, 36), (255, 255, 255), (23, 161, 117), button_pelabuhan_size)
        
        button_hutan = pygame.image.load('Background/Hutan.png')
        button_hutan_size = (300, 200)
        menu_button_hutan = MenuImageButton(button_hutan, (980, 370), None, pygame.font.Font(None, 36), (255, 255, 255), (23, 161, 117), button_hutan_size)

        BACK_Button = MenuButton(image=None, pos=(340, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color=(23,161,117))
        START_Button = MenuButton(image=None, pos=(940, 660), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color=(23,161,117))

        selected_arena_name = list_arena[selected_arena] if selected_arena else "No arena Selected"
        selected_arena_text = "Selected arena: " + selected_arena_name

        selected_arena_button = MenuButton(image=None, pos=(640, 550),text_input=selected_arena_text, font=get_font(40), base_color="White", hovering_color=(23,161,117))
        selected_arena_button.update(screen)

        BACK_Button.changeColor(POSISI_MOUSE)
        START_Button.changeColor(POSISI_MOUSE)

        BACK_Button.update(screen)
        START_Button.update(screen)
        menu_button_candi.update(screen)
        menu_button_pelabuhan.update(screen)
        menu_button_hutan.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_Button.checkForInput(POSISI_MOUSE):
                    SFX.play()
                    play()
                if START_Button.checkForInput(POSISI_MOUSE):
                    SFX.play()
                    start()
                if menu_button_candi.checkForInput(POSISI_MOUSE):
                    select_arena('Background/upper_background.png')
                    global bgm_battle
                    bgm_battle = 'a'
                if menu_button_pelabuhan.checkForInput(POSISI_MOUSE):
                    select_arena('Background/Pelabuhan.png')
                    bgm_battle = 'b'
                if menu_button_hutan.checkForInput(POSISI_MOUSE):
                    select_arena('Background/Hutan.png')
                    bgm_battle = 'c'

        pygame.display.update()

def start():
    # percabangan ini buat ngecek lagu on apa of di setting, ada percabangan variabelnya disana
    if bgm_playing == True:   
        if bgm_battle == 'a':
            BGM.change_music('MAIN MENU/background_music/Candi.mp3', -1)
        elif bgm_battle == 'b':
            BGM.change_music('MAIN MENU/background_music/Pelabuhan.mp3', -1)
        elif bgm_battle == 'c':
            BGM.change_music('MAIN MENU/background_music/Hutan.mp3', -1)   

    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait_time = 90
    attack = False
    potion = False
    mous_clicked = False
    game_over = 0

    while True:

        arena_obj = PilihArena(selected_arena)
        arena_obj.show_background()
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
                            patt_sfx.play()
                            Player_obj.attack_target(Enemy_obj)
                            current_fighter += 1
                            action_cooldown = 0
                        if potion == True:
                            if Player_obj.potions > 0:
                                if Player_obj.max_health - Player_obj.health > 30:
                                    heal_amount = random.randint(5, 20)
                                else:
                                    heal_amount = Player_obj.max_health - Player_obj.health
                                phl_sfx.play()
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
                                    heal_amount = random.randint(5, 20)
                            else:
                                heal_amount = Enemy_obj.max_health - Enemy_obj.health
                            ehl_sfx.play()
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
                            eatt_sfx.play()
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    game_over = 1

            #RESET THE TURN
            if current_fighter > total_fighter:
                current_fighter = 1

        if game_over != 0:
            if game_over == 1:
                win_sfx.play(1)
                win_sfx.set_volume(0.1)
                screen.blit(win_image, (200,0))
            if game_over == -1:
                lose_sfx.play(1)
                lose_sfx.set_volume(0.1)
                screen.blit(lose_image, (150,0))
            if restart_button.draw():
                Player_obj.reset()
                Enemy_obj.reset()
                current_fighter = 1
                action_cooldown = 0
                game_over = 0
                start()
            if back_button.draw():
                # di ubah ke lagu menu lagi biar pas back lagu battle nya ga keubah jadi default
                if bgm_playing == True:
                    BGM.change_music('MAIN MENU/background_music/BGM sunda.mp3', -1)
                main_menu()
                break
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

main_menu()
