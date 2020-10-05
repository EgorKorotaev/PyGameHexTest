import pygame

from ColorConversion import Color


class Hex(pygame.sprite.Sprite):
    def __init__(self, width, height, zoom, WIDTH, HEIGHT, color):
        pygame.sprite.Sprite.__init__(self)

        self.baseColor = color.copyRGB()
        self.glare = (color - Color(10, 30, 0, True) + Color(0, 0, 10, True)).copyRGB()
        self.light = (color - Color(5, 0, 0, True) + Color(0, 0, 5, True)).copyRGB()
        self.penumbra = (color - Color(0, 0, 20, True) + Color(5, 5, 0, True)).copyRGB()
        self.ownShadow = (color - Color(0, 0, 40, True) + Color(10, 10, 0, True)).copyRGB()
        # self.contour = (color - Color(0, 0, 75, True) + Color(15, 10, 0, True)).copyRGB()
        self.contour = self.glare
        self.shadow = None

        self.image = pygame.Surface((22 * zoom, 14 * zoom))

        # pygame.draw.rect(self.image, (255, 255, 255), (0 * zoom, 0 * zoom, 1 * zoom, 1 * zoom))
        # 1
        pygame.draw.rect(self.image, self.contour.getTuple(), (12 * zoom - zoom, 1 * zoom - zoom, 5 * zoom, 1 * zoom))
        # 2
        pygame.draw.rect(self.image, self.contour.getTuple(), (8 * zoom - zoom, 2 * zoom - zoom, 4 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (12 * zoom - zoom, 2 * zoom - zoom, 5 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.contour.getTuple(), (17 * zoom - zoom, 2 * zoom - zoom, 2 * zoom, 1 * zoom))
        # 3
        pygame.draw.rect(self.image, self.contour.getTuple(), (5 * zoom - zoom, 3 * zoom - zoom, 3 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (8 * zoom - zoom, 3 * zoom - zoom, 11 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.contour.getTuple(), (19 * zoom - zoom, 3 * zoom - zoom, 2 * zoom, 1 * zoom))
        # 4
        pygame.draw.rect(self.image, self.contour.getTuple(), (4 * zoom - zoom, 4 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (5 * zoom - zoom, 4 * zoom - zoom, 16 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.contour.getTuple(), (21 * zoom - zoom, 4 * zoom - zoom, 2 * zoom, 1 * zoom))
        # 5
        pygame.draw.rect(self.image, self.contour.getTuple(), (3 * zoom - zoom, 5 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (4 * zoom - zoom, 5 * zoom - zoom, 18 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (22 * zoom - zoom, 5 * zoom - zoom, 1 * zoom, 1 * zoom))
        # 6
        pygame.draw.rect(self.image, self.contour.getTuple(), (2 * zoom - zoom, 6 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (3 * zoom - zoom, 6 * zoom - zoom, 18 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (21 * zoom - zoom, 6 * zoom - zoom, 2 * zoom, 1 * zoom))
        # 7
        pygame.draw.rect(self.image, self.contour.getTuple(), (1 * zoom - zoom, 7 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (2 * zoom - zoom, 7 * zoom - zoom, 18 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (20 * zoom - zoom, 7 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.light.getTuple(), (21 * zoom - zoom, 7 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (22 * zoom - zoom, 7 * zoom - zoom, 1 * zoom, 1 * zoom))
        # 8
        pygame.draw.rect(self.image, self.contour.getTuple(), (1 * zoom - zoom, 8 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (2 * zoom - zoom, 8 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (3 * zoom - zoom, 8 * zoom - zoom, 16 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (19 * zoom - zoom, 8 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.light.getTuple(), (20 * zoom - zoom, 8 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (22 * zoom - zoom, 8 * zoom - zoom, 1 * zoom, 1 * zoom))
        # 9
        pygame.draw.rect(self.image, self.contour.getTuple(), (1 * zoom - zoom, 9 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.ownShadow.getTuple(), (2 * zoom - zoom, 9 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (3 * zoom - zoom, 9 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (5 * zoom - zoom, 9 * zoom - zoom, 11 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (16 * zoom - zoom, 9 * zoom - zoom, 3 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.light.getTuple(), (19 * zoom - zoom, 9 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (21 * zoom - zoom, 9 * zoom - zoom, 1 * zoom, 1 * zoom))
        # 10
        pygame.draw.rect(self.image, self.contour.getTuple(), (1 * zoom - zoom, 10 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.ownShadow.getTuple(), (2 * zoom - zoom, 10 * zoom - zoom, 3 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (5 * zoom - zoom, 10 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.baseColor.getTuple(), (7 * zoom - zoom, 10 * zoom - zoom, 5 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (12 * zoom - zoom, 10 * zoom - zoom, 4 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.penumbra.getTuple(),
                         (16 * zoom - zoom, 10 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (18 * zoom - zoom, 10 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.light.getTuple(),
                         (19 * zoom - zoom, 10 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (20 * zoom - zoom, 10 * zoom - zoom, 1 * zoom, 1 * zoom))
        # 11
        pygame.draw.rect(self.image, self.glare.getTuple(), (2 * zoom - zoom, 11 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.ownShadow.getTuple(), (3 * zoom - zoom, 11 * zoom - zoom, 4 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (7 * zoom - zoom, 11 * zoom - zoom, 5 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.penumbra.getTuple(),
                         (12 * zoom - zoom, 11 * zoom - zoom, 6 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (18 * zoom - zoom, 11 * zoom - zoom, 2 * zoom, 1 * zoom))
        # 12
        pygame.draw.rect(self.image, self.glare.getTuple(), (3 * zoom - zoom, 12 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.ownShadow.getTuple(), (5 * zoom - zoom, 12 * zoom - zoom, 3 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (8 * zoom - zoom, 12 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.penumbra.getTuple(), (9 * zoom - zoom, 12 * zoom - zoom, 7 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (16 * zoom - zoom, 12 * zoom - zoom, 3 * zoom, 1 * zoom))
        # 13
        pygame.draw.rect(self.image, self.glare.getTuple(), (5 * zoom - zoom, 13 * zoom - zoom, 2 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.ownShadow.getTuple(), (7 * zoom - zoom, 13 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (8 * zoom - zoom, 13 * zoom - zoom, 1 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.penumbra.getTuple(), (9 * zoom - zoom, 13 * zoom - zoom, 3 * zoom, 1 * zoom))
        pygame.draw.rect(self.image, self.glare.getTuple(), (12 * zoom - zoom, 13 * zoom - zoom, 4 * zoom, 1 * zoom))
        # 14
        pygame.draw.rect(self.image, self.glare.getTuple(), (7 * zoom - zoom, 14 * zoom - zoom, 5 * zoom, 1 * zoom))

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (width * zoom, height * zoom)
        self.collide_rect = self.rect
        self.speedX = 0
        self.speedY = 0
        self.width = WIDTH
        self.height = HEIGHT

    def update(self):
        self.speedX = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedX -= 4
        if keystate[pygame.K_RIGHT]:
            self.speedX += 4
        if keystate[pygame.K_UP]:
            self.speedY -= 4
        if keystate[pygame.K_DOWN]:
            self.speedY += 4
        self.rect.x += self.speedX
        self.rect.y += self.speedY

    def movement(self, key):
        if key == 'up':
            self.rect.y -= 3
        if key == 'down':
            self.rect.y += 3
