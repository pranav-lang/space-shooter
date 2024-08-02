import pygame
import random
from shooter import Shooter
from alien import Alien

# Initialize pygame
pygame.init()

# Initialize the mixer (sound system) before using any sound-related features
pygame.mixer.init(44100, -16, 2, 2048)

# CONSTANTS
SHOOT_SOUND = pygame.mixer.Sound('./assets/shot.wav')  # Ensure the correct path and file name
SHOOT_SOUND.set_volume(0.2)
milliseconds_delay = 2000  # 2 seconds
bullet_event = pygame.USEREVENT + 1
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('GAME OVER!!', True, (255, 0, 0))
pygame.time.set_timer(bullet_event, milliseconds_delay)

# Define screen dimensions
screen = pygame.display.set_mode((580, 580))

# Set the caption of the screen
pygame.display.set_caption('Alien Shooter')

# Initial position for the shooter
SHOOTER_INIT_POS = (100, screen.get_height() - 50)

# Define the background color using RGB color coding.
background_colour = (0, 0, 0)

# Load shooter image and initialize shooter
shooter_img = pygame.image.load('./assets/shooter2.png').convert_alpha()
shooter_img = pygame.transform.scale(shooter_img, (40, 40))
shooter = Shooter(SHOOTER_INIT_POS[0], SHOOTER_INIT_POS[1], 50, 50, shooter_img)

# Load alien image and initialize alien
aliens = []
alien_img = pygame.image.load('./assets/alien2.png').convert_alpha()
alien_img = pygame.transform.scale(alien_img, (40, 40))
pos_x = [random.randint(0, 400) for _ in range(10)]

for i in range(10):
    alien = Alien(pos_x[i], -10, 40, 40, alien_img)
    aliens.append(alien)

# RANDOM STARS POSITION GENERATOR
rand_x = [random.randint(0, 580) for _ in range(100)]
rand_y = [random.randint(0, 580) for _ in range(100)]
random_star_pos = [(x, y) for x, y in zip(rand_x, rand_y)]
random_size = [random.randint(1, 2) for _ in range(100)]

# Clock object to manage frame rate
clock = pygame.time.Clock()

# Game loop
running = True

while running:
    screen.fill(background_colour)

    # DRAW STARS
    for pos, size in zip(random_star_pos, random_size):
        pygame.draw.circle(screen, (255, 255, 255), pos, size)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if shooter.alive:
                    SHOOT_SOUND.play()
                    shooter.shoot()
        elif event.type == bullet_event:
            for alien in aliens:
                alien.shoot()

    # Handle continuous movement based on key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shooter.move_left()
    if keys[pygame.K_RIGHT]:
        shooter.move_right(screen.get_width())
    if keys[pygame.K_UP]:
        shooter.move_up()
    if keys[pygame.K_DOWN]:
        shooter.move_down(screen.get_height())

    # Draw the shooter and bullets
    shooter.draw(screen, aliens)

    # Draw the alien
    for alien in aliens:
        alien.draw(screen, shooter)
        alien.move_down(screen.get_width())

    if not shooter.alive:
        # Display the "GAME OVER" text
        screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame when the loop is over
pygame.quit()
