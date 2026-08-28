import pygame
import random
import sys

# Pygame-ni ishga tushirish
pygame.init()

# Ekran va ranglar
WIDTH, HEIGHT = 700, 400
BG_COLOR = (15, 10, 25)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
PURPLE = (150, 0, 255)
ORANGE = (255, 120, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("44. Quantum Dash")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Ikki yo'lak (Tepada va Pastda)
LANE_TOP_Y = 100
LANE_BOTTOM_Y = 280

player = pygame.Rect(100, LANE_BOTTOM_Y, 30, 30)
current_lane = "bottom"  # "top" yoki "bottom"

obstacles = []
spawn_timer = 0
score = 0
speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Teleportatsiya (Yo'lakni almashtirish)
                if current_lane == "bottom":
                    current_lane = "top"
                    player.y = LANE_TOP_Y
                else:
                    current_lane = "bottom"
                    player.y = LANE_BOTTOM_Y

    # To'siqlar yaratish
    spawn_timer += 1
    if spawn_timer >= 45:
        lane = random.choice(["top", "bottom"])
        obs_y = LANE_TOP_Y if lane == "top" else LANE_BOTTOM_Y
        obstacles.append(pygame.Rect(WIDTH, obs_y, 30, 30))
        spawn_timer = 0

    # To'siqlar harakati va to'qnashuv
    for obs in obstacles[:]:
        obs.x -= speed

        if obs.colliderect(player):
            pygame.quit()
            sys.exit()

        if obs.right < 0:
            obstacles.remove(obs)
            score += 10

    # Chizish
    screen.fill(BG_COLOR)

    # Yo'lak chiziqlari
    pygame.draw.line(screen, PURPLE, (0, LANE_TOP_Y + 35), (WIDTH, LANE_TOP_Y + 35), 4)
    pygame.draw.line(screen, PURPLE, (0, LANE_BOTTOM_Y + 35), (WIDTH, LANE_BOTTOM_Y + 35), 4)

    # To'siqlar
    for obs in obstacles:
        pygame.draw.rect(screen, ORANGE, obs, border_radius=6)

    # O'yinchi
    pygame.draw.rect(screen, CYAN, player, border_radius=8)

    # Hisob
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)