import pymunk
from block import Block

class Shape():
    def __init__(self, pos, size, COLLTYPE, space, type=pymunk.Body.DYNAMIC, mass=0.3, typeIn=None):
        self.pos = pos
        self.type = typeIn
        self.blocks = []
        

        if self.type == None:
            self.blocks.append(Block(pos, size, COLLTYPE, space))

        elif self.type == 'I':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x, y+20), size, COLLTYPE, space)
            b3 = Block((x, y+40), size, COLLTYPE, space)
            b4 = Block((x, y+60), size, COLLTYPE, space)

            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))
            
        elif self.type == 'J':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x, y+20), size, COLLTYPE, space)
            b3 = Block((x, y+40), size, COLLTYPE, space)
            b4 = Block((x-20, y+40), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'L':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x, y+20), size, COLLTYPE, space)
            b3 = Block((x, y+40), size, COLLTYPE, space)
            b4 = Block((x+20, y+40), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'O':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x, y+20), size, COLLTYPE, space)
            b3 = Block((x+20, y+20), size, COLLTYPE, space)
            b4 = Block((x+20, y), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'S':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x-20, y), size, COLLTYPE, space)
            b3 = Block((x-20, y+20), size, COLLTYPE, space)
            b4 = Block((x-40, y+20), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'T':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x+20, y), size, COLLTYPE, space)
            b3 = Block((x+40, y), size, COLLTYPE, space)
            b4 = Block((x+20, y+20), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'Z':
            x, y = pos
            b1 = Block((x, y), size, COLLTYPE, space)
            b2 = Block((x+20, y), size, COLLTYPE, space)
            b3 = Block((x+20, y+20), size, COLLTYPE, space)
            b4 = Block((x+40, y+20), size, COLLTYPE, space)
            
            b1.connect_to_block(b2)
            b1.connect_to_block(b3)
            b1.connect_to_block(b4)
            
            b2.connect_to_block(b3)
            b2.connect_to_block(b4)

            b3.connect_to_block(b4)
            self.blocks.extend((b1, b2, b3, b4))

        elif self.type == 'border':
            self.blocks.append(Block((400,610), (800,20), COLLTYPE, space, type=pymunk.Body.STATIC))
            self.blocks.append(Block((-10,300), (20,600), COLLTYPE, space, type=pymunk.Body.STATIC))
            self.blocks.append(Block((810,300), (20,600), COLLTYPE, space, type=pymunk.Body.STATIC))
            self.blocks.append(Block((400,-10), (800,20), COLLTYPE, space, type=pymunk.Body.STATIC))