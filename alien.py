
import pygame
import threading
class Alien:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = img
        self.speed = 0.5
        self.width = width
        self.height = height
        self.alive = True
        self.lock = threading.Lock()

        # Bullet properties
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (220 ,40 ,20)
        self.bullet_vel = 3
        self.bullets = []

    def draw(self, window , shooter):
        if self.alive:
            window.blit(self.img, (self.x, self.y))
            pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height) , 3)

        self.draw_bullets(window,shooter)

    def draw_bullets(self, window,shooter):
        for bullet in self.bullets:
            pygame.draw.rect(window, self.bullet_color, pygame.Rect(bullet[0], bullet[1], self.bullet_width, self.bullet_height))
            bullet[1] += self.bullet_vel

            if((bullet[1] + self.bullet_height >= shooter.y) and ((bullet[0]  + self.bullet_width >= shooter.x) and (bullet[0] <= shooter.x + shooter.width ))):
                shooter.alive = False
        self.bullets = [bullet for bullet in self.bullets if bullet[1] < window.get_height()]



    def shoot(self):

        bullet_x = self.x + self.width // 2  - self.bullet_width
        bullet_y = self.y + self.height
        self.bullets.append([bullet_x, bullet_y])

    def get_bullets(self):
        return self.bullets




    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self, screen_width):
        if self.x < screen_width - self.width:
            self.x += self.speed

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self, screen_height):
        if self.y < screen_height - self.height:
            self.y += self.speed
