import pygame
import pymunk
from game import Game
import math
from block import Block

pygame.init()

pygame.display.set_caption('Phystris')

screen = pygame.display.set_mode((800, 600))

myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()

clock = pygame.time.Clock()

def render():
    screen.fill((0,0,0))

    for s in game.shapes:
        pygame.draw.polygon(screen, s.shape.color, s.wordlVertices())

while not done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
    
    pressed = pygame.key.get_pressed()

    game.tick()
    render()

    pygame.display.flip()
    clock.tick(60)
    