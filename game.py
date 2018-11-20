import pymunk
from block import Block
from shape import Shape
import random
class Game():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 450.0)
        self.space.collision_slob = 0

        self.shapes = []
        self.joints = []

        COLLTYPE_SHAPE = 0
        COLLTYPE_BORDER = 1

        h1 = self.space.add_collision_handler(COLLTYPE_SHAPE, COLLTYPE_BORDER)
        h1.begin = self.border_col
        h2 = self.space.add_collision_handler(COLLTYPE_SHAPE, COLLTYPE_SHAPE)
        h2.begin = self.shape_col
        self.shapes.append(Shape((0,0), (0,0), COLLTYPE_BORDER, self.space, typeIn='border'))
        
        for s in self.shapes:
            for b in s.blocks:
                b.elasticity = 0
                b.friction = 1

        self.cur_shape = Shape((400,500), (20,20), COLLTYPE_SHAPE, self.space, typeIn='T')
        self.shapes.append(self.cur_shape)
        '''
        self.shapes.append(Shape((40,300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='I'))
        self.shapes.append(Shape((100, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='J'))
        self.shapes.append(Shape((200, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='L'))
        self.shapes.append(Shape((300, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='O'))
        self.shapes.append(Shape((400, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='S'))
        self.shapes.append(Shape((500, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='T'))
        self.shapes.append(Shape((600, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='Z'))
        '''
        self.state = 0
        
    
    def tick(self):
        self.space.step(1/60.0)

    def start_game(self):
        self.state = 1
        
    def stop_game(self):
        self.state = 99
    
    def border_col(self, arbiter, space, _):
        s, border = arbiter.shapes
        
        for b in self.cur_shape.blocks:
            if s == b.shape:
                self.new_shape()

        return True
    
    def shape_col(self, arbiter, space, _):
        s1, s2 = arbiter.shapes

        for b in self.cur_shape.blocks:
            if s1 == b.shape or s2 == b.shape:
                self.new_shape()
        
        return True
    
    def new_shape(self):
        type = self.get_random_type()
        s = Shape((400, 100), (20,20), 0, self.space, typeIn=type)
        self.shapes.append(s)
        self.cur_shape = s
    
    def get_random_type(self):
        r = random.randint(0,6)

        if r == 0:
            return 'I'
        elif r == 1:
            return 'J'
        elif r == 2:
            return 'L'
        elif r == 3:
            return 'O'
        elif r == 4:
            return 'S'
        elif r == 5:
            return 'T'
        elif r == 6:
            return 'Z'