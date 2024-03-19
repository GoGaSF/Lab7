import pygame
import os


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Музыкальный проигрыватель")

# Директория с музыкальными файлами
MUSIC_DIR = "music"

# Функция загрузки музыки
def load_music(file_path):
    pygame.mixer.music.load(file_path)

# Функция воспроизведения музыки
def play_music():
    pygame.mixer.music.play()

# Функция остановки музыки
def stop_music():
    pygame.mixer.music.stop()

# Функция перехода к следующей композиции
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    load_music(os.path.join(MUSIC_DIR, music_files[current_track_index]))
    play_music()

# Функция перехода к предыдущей композиции
def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    load_music(os.path.join(MUSIC_DIR, music_files[current_track_index]))
    play_music()

# Список музыкальных файлов
music_files = os.listdir(MUSIC_DIR)
current_track_index = 0

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

pygame.quit()
