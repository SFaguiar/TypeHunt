import pygame
import math

pygame.init()
FPS = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/font/Roboto-Regular.ttf')
WIDTH = 640
HEIGHT = 768
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
level = 0

for i in range(1, 4):
    bgs.append(pygame.image.load(f'assets/bg/{i}.png'))