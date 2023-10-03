import pygame
import math
from sys import exit

# Cria uma classe chamado target com as coordenadas x e y e a imagem do objeto:
class Target:
    def __init__(self, x0:int, y0:int, x_speed:int, y_speed:int, image_path:str):
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.rectangle = self.surface.get_rect(midbottom = (x0, y0))
        self.x_speed = x_speed
        self.y_speed = y_speed

    
    def move_target(self, delta_x:int, delta_y:int):
        x = self.rectangle.midbottom[0] + delta_x
        y = self.rectangle.midbottom[1] + delta_y
        self.rectangle.midbottom = (x, y)
        
    
    def move_target_to(self, x:int, y:int):
        self.x = x
        self.y = y

pygame.init()
# Cria a janela principal
screen = pygame.display.set_mode((768, 640))
pygame.display.set_caption("TypeHunt")
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/RobotoMono-Regular.ttf', 32)

background_sky = pygame.image.load('assets/graphics/backgrounds/level_2/sky.png').convert_alpha()
background_sky = pygame.transform.scale(background_sky, (768, 640))
background_ground = pygame.image.load('assets/graphics/backgrounds/level_2/ground.png').convert_alpha()
background_ground = pygame.transform.scale(background_ground, (768, 640))

text_surface = font.render('Hello World!', False, 'black')

# Cria os objetos do tipo alvo:
alvo_1 = Target(300, 640, 4, 4, 'assets/graphics/targets/black_duck_diagonal_1.png')
alvo_1.surface = pygame.transform.scale(alvo_1.surface, (64, 64))
alvo_1.rectangle = alvo_1.surface.get_rect()


# Inicializa o mouse:
mouse = pygame.mouse

# Loop principal.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if alvo_1.rectangle.collidepoint(event.pos):
                print('Acertou!')
    
    
    # Renderiza os fundos:        
    screen.blit(background_sky, (0, 0))
    screen.blit(background_ground, (0, 0))
    
    # Renderiza os textos:
    screen.blit(text_surface, (0, 0))

    # Renderiza os objetos:
    screen.blit(alvo_1.surface, alvo_1.rectangle)
    
    if alvo_1.rectangle.left <= 0:
        alvo_1.x_speed = abs(alvo_1.x_speed)
    elif alvo_1.rectangle.right >= 768:
        alvo_1.x_speed *= -1
        
    if alvo_1.rectangle.top <= 0:
        alvo_1.y_speed = abs(alvo_1.x_speed)
    elif alvo_1.rectangle.bottom>= 640:
        alvo_1.y_speed *= -1
        
    # Move os objetos:
    alvo_1.move_target(alvo_1.x_speed, alvo_1.y_speed)
    
    pygame.display.update()
    clock.tick(60)