import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перемещение шарика")

# Установка цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Установка параметров шара
radius = 25
x = (WIDTH - radius) // 2
y = (HEIGHT - radius) // 2
speed = 20

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - speed >= 0:
                    y -= speed
            elif event.key == pygame.K_DOWN:
                if y + speed <= HEIGHT - radius:
                    y += speed
            elif event.key == pygame.K_LEFT:
                if x - speed >= 0:
                    x -= speed
            elif event.key == pygame.K_RIGHT:
                if x + speed <= WIDTH - radius:
                    x += speed

    pygame.display.flip()

    # Ограничение частоты обновления экрана
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
