import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_INSTANCES = 5

color_name = input("What color would you like for the background (pink, white, or black)?: ").lower().strip()

if color_name == "pink":
    BACKGROUND_COLOR = (240, 192, 203)
elif color_name == "white":
    BACKGROUND_COLOR = (255, 255, 255)
elif color_name == "black":
    BACKGROUND_COLOR = (0, 0, 0)
else:
    print("Invalid color. Defaulting to pink.")
    BACKGROUND_COLOR = (240, 192, 203)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cinnamoroll yippieee")
clock = pygame.time.Clock()

img = pygame.image.load("Cinnamoroll2Bbackground.webp").convert_alpha()
img = pygame.transform.scale(img, (100, 100))

class Cinnamoroll:
    def __init__(self):
        self.image = img.copy()
        scale = random.randint(80, 120)
        self.image = pygame.transform.scale(self.image, (scale, scale))

        self.x = random.randint(0, SCREEN_WIDTH - scale)
        self.y = random.randint(0, SCREEN_HEIGHT - scale)
        self.speed_x = random.uniform(1, 4)
        self.speed_y = random.uniform(1, 3)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self):
        self.x += self.speed_x * self.direction_x
        self.y += self.speed_y * self.direction_y

        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.image.get_width():
            self.direction_x *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - self.image.get_height():
            self.direction_y *= -1

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

instances = [Cinnamoroll() for _ in range(NUM_INSTANCES)]

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for instance in instances:
        instance.update()
        instance.draw(screen)

    pygame.display.flip()

pygame.quit()