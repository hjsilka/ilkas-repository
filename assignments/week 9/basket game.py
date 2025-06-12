import pygame
import random

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cupcake Catcher")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# images
hello_kitty_img = pygame.image.load("hello_kitty.png")
hello_kitty_img = pygame.transform.scale(hello_kitty_img, (80, 60))

cupcake_img = pygame.image.load("cupcake.png")
cupcake_img = pygame.transform.scale(cupcake_img, (40, 40))

rotten_food_img = pygame.image.load("rotten_food.png")
rotten_food_img = pygame.transform.scale(rotten_food_img, (40, 40))

# classes

class FallingItem:
    def __init__(self, x, y, speed, image):
        self._x = x
        self._y = y
        self._speed = speed
        self._image = image

    def update(self, slow_factor=1):
        self._y += self._speed * slow_factor

    def draw(self, surface):
        surface.blit(self._image, (self._x, self._y))

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._image.get_width(), self._image.get_height())

    def get_y(self):
        return self._y


class Cupcake(FallingItem):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed, cupcake_img)


class RottenFood(FallingItem):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed, rotten_food_img)

# class for player
class Player:
    def __init__(self):
        self._x = SCREEN_WIDTH // 2
        self._y = SCREEN_HEIGHT - 70
        self._speed = 10
        self._image = hello_kitty_img

    def move(self, dx):
        self._x += dx
        self._x = max(0, min(self._x, SCREEN_WIDTH - self._image.get_width()))

    def draw(self, surface):
        surface.blit(self._image, (self._x, self._y))

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._image.get_width(), self._image.get_height())

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed


# functions
# game instructions at start
def show_instructions():
    screen.fill((255, 192, 203))
    lines = [
        "Hello Kitty is trying to collect as many cupcakes",
        "as possible for her friends.",
        "Can you help her?",
        "Make sure not to catch any rotten ones!",
        "Move with Left/Right Arrows.",
        "Click anywhere to start!",
    ]

    screen.fill((255, 192, 203))
    for i, line in enumerate(lines):
        text_surf = font.render(line, True, (0, 0, 0))
        screen.blit(text_surf, (50, 100 + i * 40))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


# game over screen
def game_over(score, rotten_hits):
    screen.fill((255, 255, 255))
    game_over_text = font.render("Game Over! You caught 3 rotten foods.", True, (255, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(4000)

    pygame.quit()
    exit()

# main game loop
def main():
    show_instructions()
    player = Player()
    items = []
    score = 0
    combo = 0
    rotten_hits = 0

    running = True
    frame_count = 0

    while running:
        dt = clock.tick(FPS)
        frame_count += 1
        screen.fill((255, 255, 255))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.get_speed())
        if keys[pygame.K_RIGHT]:
            player.move(player.get_speed())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if frame_count % 30 == 0:
            item_type = random.choice([Cupcake, RottenFood])
            items.append(item_type(random.randint(0, SCREEN_WIDTH - 40), 0, random.randint(3, 6)))

        for item in items[:]:
            item.update(1)
            item.draw(screen)

            if item.get_rect().colliderect(player.get_rect()):
                if isinstance(item, Cupcake):
                    combo += 1
                    score += 10 * combo
                else:
                    combo = 0
                    score -= 20
                    rotten_hits += 1
                    if rotten_hits >= 3:
                        running = False
                items.remove(item)

            elif item.get_y() > SCREEN_HEIGHT:
                items.remove(item)
                combo = 0

        player.draw(screen)
        score_text = font.render(f"Score: {score}  Combo: x{combo}  Rotten caught: {rotten_hits}/3", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    game_over(score, rotten_hits)


if __name__ == "__main__":
    main()

# You try to catch as many cupcakes for Hello Kitty as possible
# You start by clicking anywhere on the screen and move with the right/left arrow keys
# If you catch 3 rotten foods the game stops and closes after 4 seconds
# You can achive more points by scoring combos (catching multiple cupcakes in a row)

