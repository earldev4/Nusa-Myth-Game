import pygame, sys
from subprocess import call
from menu_button import Button
from pygame import mixer

pygame.init()
pygame.mixer.init()

DISPLAY = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nusa Myth")

mixer.music.load('MAIN MENU/background_music/BGM sunda.mp3')
mixer.music.play(-1)

SFX = pygame.mixer.Sound("MAIN MENU/background_music/SFX angklung.mp3")

BACKGROUND = pygame.image.load("MAIN MENU/background/Brick_Background.png")

def get_font(size):
    return pygame.font.Font("MAIN MENU/menu_font/font2.ttf", size)
def get_credit_font(size):
    return pygame.font.Font("MAIN MENU/menu_font/font1.ttf", size)
def launch():
    pygame.quit()
    call(["python", "Main.py"])

def play():
    #untuk membuka window utama(Main.py)
    launch()

bgm_playing = True 

def options():
    global bgm_playing 
    SFX.play()
    while True:
        POSISI_MOUSE = pygame.mouse.get_pos()

        DISPLAY.blit(BACKGROUND, (0, 0))


        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color=(23,161,117))

        OPTIONS_BACK.changeColor(POSISI_MOUSE)
        OPTIONS_BACK.update(DISPLAY)

        bgm_button_text = "Turn Music Off" if bgm_playing else "Turn Music On"
        BGM_BUTTON = Button(image=None, pos=(640, 360), 
                            text_input=bgm_button_text, font=get_font(40), base_color="White", hovering_color=(23,161,117))

        BGM_BUTTON.changeColor(POSISI_MOUSE)
        BGM_BUTTON.update(DISPLAY)

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
                        mixer.music.pause()
                    else:
                        SFX.play()
                        mixer.music.unpause()

        pygame.display.update()

def credit():
    SFX.play()
    while True:
        CREDIT_MOUSE_POS = pygame.mouse.get_pos()

        DISPLAY.blit(BACKGROUND, (0, 0))

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
            DISPLAY.blit(credit_text, credit_rect)
            y_offset += 50

        CREDIT_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_credit_font(40), base_color="White", hovering_color=(23,161,117))

        CREDIT_BACK.changeColor(CREDIT_MOUSE_POS)
        CREDIT_BACK.update(DISPLAY)

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
        DISPLAY.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        main_menu_title = pygame.image.load("MAIN MENU/object/Nusa Myth.png")
        MENU_RECT = main_menu_title.get_rect(center=(640, 100))
        
        PLAY_BUTTON = Button(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 275), 
                            text_input="PLAY", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)
        OPTIONS_BUTTON = Button(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 400), 
                            text_input="SETTINGS", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)
        CREDIT_BUTTON = Button(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 525), 
                            text_input="CREDIT", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)

        QUIT_BUTTON = Button(image=pygame.image.load("MAIN MENU/object/Brick.png"), pos=(640, 650), 
                            text_input="QUIT", font=get_font(80), base_color="White", hovering_color=(32, 30, 29),text_y_offset=10)

        DISPLAY.blit(main_menu_title, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, CREDIT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(DISPLAY)
        
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

main_menu()