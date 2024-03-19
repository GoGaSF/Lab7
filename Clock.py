import pygame
import sys
import time
import math
from datetime import datetime
import pytz

# Инициализация Pygame
pygame.init()

# Определение размера экрана
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Clock")

# Определение цветов
BLACK = (0, 0, 0)

# Загрузка изображений (замените пути на свои)
background_image = pygame.image.load("background_image.png")
minute_hand_image = pygame.image.load("second_hand_image.png")
second_hand_image = pygame.image.load("minute_hand_image.png")

# Функция для рисования циферблата
def draw_clock():
    screen.blit(background_image, ((SCREEN_WIDTH - background_image.get_width()) // 2, (SCREEN_HEIGHT - background_image.get_height()) // 2))

# Функция для рисования стрелок часов
def draw_hands(angle, image):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(rotated_image, rotated_rect)

# Функция для получения текущего времени в Алматы
def get_current_time_in_almaty():
    tz = pytz.timezone('Asia/Almaty')
    return datetime.now(tz)

# Основной цикл программы
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = get_current_time_in_almaty()
        seconds_angle = (current_time.second / 60) * 360
        minutes_angle = (current_time.minute / 60) * 360

        screen.fill(BLACK)
        draw_clock()
        draw_hands(seconds_angle, second_hand_image)
        draw_hands(minutes_angle, minute_hand_image)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
