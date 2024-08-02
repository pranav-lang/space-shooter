import pygame
from alien import Alien


pygame.mixer.init(44100, -16, 2, 2048)

# CONSTANTS
KILL_SOUND = pygame.mixer.Sound('./assets/kill.mp3')  # Ensure the correct path and file name
KILL_SOUND.set_volume(0.2)

class Shooter:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = img
        self.speed = 4
        self.width = width
        self.height = height
        self.alive = True

        # Bullet properties
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (166, 253, 41)
        self.bullet_vel = 10
        self.bullets = []

    def draw(self, window , aliens):

        if self.alive:
            window.blit(self.img, (self.x, self.y))
            pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height) , 3)
        self.draw_bullets(window,aliens)

    def draw_bullets(self, window,aliens):
        for bullet in self.bullets:
            pygame.draw.rect(window, self.bullet_color, pygame.Rect(bullet[0], bullet[1], self.bullet_width, self.bullet_height))
            bullet[1] -= self.bullet_vel  # Move the bullet upward

            for alien in aliens:
                if((alien.y + alien.height >= bullet[1]) and (alien.x <= bullet[0] and (bullet[0] <= alien.x + alien.width)) ):
                    KILL_SOUND.play()
                    aliens.remove(alien)
            # CHECK COLLISONS

        # Remove bullets that are off the screen
        self.bullets = [bullet for bullet in self.bullets if bullet[1] > 0]




    def shoot(self):
        # Add a new bullet from the center top of the shooter
        bullet_x = self.x + self.width // 2  - self.bullet_width
        bullet_y = self.y
        self.bullets.append([bullet_x, bullet_y])





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
