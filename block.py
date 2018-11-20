import pymunk
from pymunk import Vec2d
import random

class Block():
    def __init__(self, pos, size, COLLTYPE, space, type=pymunk.Body.DYNAMIC, mass=0.3):
        l, h = size
        moment = 1000
        self.space = space
        self.body = pymunk.Body(mass, moment, type)
        self.body.position = Vec2d(pos)
        self.shape = pymunk.Poly.create_box(self.body, (l, h))
        self.shape.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.shape.friction = 0.3
        self.shape.elasticity = 0
        self.shape.collision_type = COLLTYPE
        self.space.add(self.body, self.shape)


        self.joints = []


    def wordl_vertices(self):
        vertices = []
        for v in self.shape.get_vertices():
            x, y = v.rotated(self.shape.body.angle) + self.shape.body.position
            vertices.append(Vec2d(x, y))
        return vertices
    
    def connect_to_block(self, block):
        j1 = pymunk.constraint.PinJoint(self.body, block.body, anchor_a=(20,0), anchor_b=(-20,0))
        j2 = pymunk.constraint.PinJoint(self.body, block.body, anchor_a=(-20,0), anchor_b=(20,0))
        j3 =pymunk.constraint.PinJoint(self.body, block.body)
        self.joints.extend((j1, j2, j3))
        #block.joints.extend((j1, j2, j3))
    
        for i in range(1,3):
            self.joints[-i].error_bias = pow(1.0 - 0.5, 60.0)

        self.space.add(self.joints[-1])
        self.space.add(self.joints[-2])
        self.space.add(self.joints[-3])
    
    def delete(self):
        self.space.remove(self.shape, self.body)


