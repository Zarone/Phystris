import pymunk
from pymunk import Vec2d
import math
import random

class Block():
    def __init__(self, pos, size, COLLTYPE, space, type=pymunk.Body.DYNAMIC, mass=0.3):
        l, h = size
        moment = 1000
        self.body = pymunk.Body(mass, moment, type)
        self.body.position = Vec2d(pos)
        self.shape = pymunk.Poly.create_box(self.body, (l, h))
        self.shape.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.shape.friction = 0.1
        self.shape.elasticity = 0
        self.shape.collision_type = COLLTYPE
        space.add(self.body, self.shape)


    def wordlVertices(self):
        vertices = []
        for v in self.shape.get_vertices():
            x, y = v.rotated(self.shape.body.angle) + self.shape.body.position
            vertices.append(Vec2d(x, y))
        return vertices

        

