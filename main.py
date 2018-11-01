import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((800, 600))

myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
    
    pressed = pygame.key.get_pressed()
    
    game.tick()
    game.render()

    pygame.display.flip()
    clock.tick(60)
    