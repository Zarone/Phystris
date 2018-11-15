import pymunk
import math
from block import Block

class Game():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 700.0)
        self.space.collision_slob = 0

        self.shapes = []

        COLLTYPE_SHAPE = 0
        COLLTYPE_BORDER = 1

        self.shapes.append(Block((400,610), (800,20), COLLTYPE_BORDER, self.space, type=pymunk.Body.STATIC))
        self.shapes.append(Block((-10,300), (20,300), COLLTYPE_BORDER, self.space, type=pymunk.Body.STATIC))
        self.shapes.append(Block((810,300), (20,300), COLLTYPE_BORDER, self.space, type=pymunk.Body.STATIC))
        self.shapes.append(Block((400,-10), (800,20), COLLTYPE_BORDER, self.space, type=pymunk.Body.STATIC))
        
        for s in self.shapes:
            s.shape.elasticity = 0
            s.shape.friction = 1

        self.shapes.append(Block((400,300), (20, 20), COLLTYPE_SHAPE, self.space, mass=1))
        self.shapes.append(Block((500,275), (200, 20), COLLTYPE_SHAPE, self.space, mass=1))

        self.state = 0
        
    
    def tick(self):
        self.space.step(1/60.0)

    def start_game(self):
        self.state = 1
        
    def stop_game(self):
        self.state = 99