import pygame

from ColorConversion import Color
from HexMap import HexMapStorage
from Player import Player

WIDTH = 640
HEIGHT = 640
ZOOM = 16
FPS = 60

# Задаем цвета
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Создаём поверхность на которой будет отрисовка всего
hexMapSurface = pygame.Surface((WIDTH - 2 * ZOOM, HEIGHT - 2 * ZOOM))
# Устанавливаем прозрачный фон
hexMapSurface.set_colorkey(0)

# Создаём группу спрайтов гексов поля
hexMapSprite = pygame.sprite.Group()
hexMapStorage = HexMapStorage(hexMapSprite, "gray")
hexMapStorage.initializationDefaultSprite(ZOOM, WIDTH, HEIGHT)

allEntity = pygame.sprite.Group()
player = Player(GREEN, WIDTH, HEIGHT)
allEntity.add(player)

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
                # for hex in hexMapSprite:
                #     if hex.collide_rect(hex.rect, event.pos):
                #         hex.movement('up')
            if event.button == 2:
                pass
            if event.button == 4:
                ZOOM += 1
                for i in hexMapSprite:
                    i.draw(ZOOM)
            if event.button == 5:
                ZOOM -= 1
                for i in hexMapSprite:
                    i.draw(ZOOM)

    # Заливка предыдущего кадра цветом
    hexMapSurface.fill((0, 0, 0))
    screen.fill((232, 232, 237))

    # Действие каждого элемента группы
    hexMapSprite.update()
    allEntity.update()

    # Отрисовка
    hexMapSprite.draw(screen)
    allEntity.draw(screen)
    screen.blit(hexMapSurface, (ZOOM, ZOOM))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
