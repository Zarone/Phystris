import pygame
from game import Game
from block import Block
from shape import Shape

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
        for b in s.blocks:
            pygame.draw.polygon(screen, b.shape.color, b.wordl_vertices())

while not done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    game.shapes.append(Shape(pos, (20,20,), 0, game.space))
                
                if event.type == pygame.KEYUP and event.key == pygame.K_p:
                    for b in game.shapes[-1].blocks:
                        b.delete()
                    game.shapes.pop(-1)
                    

    pressed = pygame.key.get_pressed()

    game.tick()
    render()

    pygame.display.flip()
    clock.tick(60)
    