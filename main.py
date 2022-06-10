import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
r = pygame.Rect(0, 0, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)
pos = (300, 300)
pygame.draw.circle(screen, (255, 0, 0), pos, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('happy end')
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key == pygame.K_SPACE)
            pygame.draw.circle(screen, (0, 255, 0), pos, 20)
    pygame.display.flip()


