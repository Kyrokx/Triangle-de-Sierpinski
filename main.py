import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

width = screen.get_width()  # x
height = screen.get_height()  # y

reduction = (1 / 2)
r = 8  # Number of recursion

p_1 = pygame.math.Vector2(height * (1 / 4), width * (2 / 3))
p_2 = pygame.math.Vector2(height * (3 / 4), width * (2 / 3))
p_3 = pygame.math.Vector2(height / 2, width * (1 / 5))

points = [p_1, p_2, p_3]


def milieu(start_x, end_x, start_y, end_y):
    return (start_x + end_x) * reduction, (start_y + end_y) * reduction


def rdm():
    return int(random.randint(0, 255))


def triangle(pos_1, pos_2, pos_3, i):
    if i == 0:
        return
    else:
        pos_p_1 = pygame.math.Vector2(milieu(pos_1.x, pos_2.x, pos_1.y, pos_2.y))
        pos_p_2 = pygame.math.Vector2(milieu(pos_2.x, pos_3.x, pos_2.y, pos_3.y))
        pos_p_3 = pygame.math.Vector2(milieu(pos_3.x, pos_1.x, pos_3.y, pos_1.y))
        # pygame.draw.polygon(screen, pygame.Color(rdm(), rdm(), rdm()), [pos_1, pos_2, pos_3], width=1)
        pygame.draw.polygon(screen, "white", [pos_1, pos_2, pos_3], width=1)
        triangle(pos_3, pos_p_2, pos_p_3, i - 1)
        triangle(pos_p_1, pos_1, pos_p_3, i - 1)
        triangle(pos_p_2, pos_p_1, pos_2, i - 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill(pygame.Color(rdm(), rdm(), rdm()))
    screen.fill("black")

    triangle(p_1, p_2, p_3, r)

    pygame.display.update()

    pygame.display.flip()

    # pygame.image.save(screen, f'./output/{str(round(time.time() * 1000))}.png') # Image saving

    clock.tick(60)

pygame.quit()
