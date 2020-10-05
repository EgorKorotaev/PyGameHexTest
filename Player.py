import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill(color.getTuple())
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.speed = 0
        self.maxSpeed = 6
        self.timer = 0
        self.width = width
        self.height = height

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_KP4]:
            if self.maxSpeed > self.speed:
                if self.timer < 60:
                    self.speed = (self.timer * 0.15) ** 2 / 1
                    self.timer += 1
        else:
            self.speed = 0
            self.timer = 0
        self.rect.x -= self.speed
        if self.rect.left > self.width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = self.width