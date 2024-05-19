import pygame

# class music, no inputan, cuma buat inisialisasi lagu (obj nya ada di line 392), ntar pake fungsinya buat play, pause, dll
class Music:
    def __init__(self):
        pygame.mixer.init()
        self.current_music = None

    def load_music(self, path):
        if self.current_music != path:
            pygame.mixer.music.load(path)
            self.current_music = path 

    def play_music(self, loop):
        pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def change_music(self, new_path, loop):
        self.stop_music()
        self.load_music(new_path)
        self.play_music(loop)