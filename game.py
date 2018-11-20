import pymunk
from block import Block
from shape import Shape
class Game():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 700.0)
        self.space.collision_slob = 0

        self.shapes = []
        self.joints = []

        COLLTYPE_SHAPE = 0
        COLLTYPE_BORDER = 1

        self.shapes.append(Shape((0,0), (0,0), COLLTYPE_BORDER, self.space, typeIn='border'))
        
        for s in self.shapes:
            for b in s.blocks:
                b.elasticity = 0
                b.friction = -1

        self.shapes.append(Shape((40,300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='I'))
        self.shapes.append(Shape((100, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='J'))
        self.shapes.append(Shape((200, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='L'))
        self.shapes.append(Shape((300, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='O'))
        self.shapes.append(Shape((400, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='S'))
        self.shapes.append(Shape((500, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='T'))
        self.shapes.append(Shape((600, 300),(20,20), COLLTYPE_SHAPE, self.space, typeIn='Z'))


        self.state = 0
        
    
    def tick(self):
        self.space.step(1/60.0)

    def start_game(self):
        self.state = 1
        
    def stop_game(self):
        self.state = 99