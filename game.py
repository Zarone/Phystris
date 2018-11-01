import pygame

class Game():
    def __init__(self):
        self.state = 0
        
    
    def tick(self):
        pass
    
    def start_game(self):
        self.state = 1
        
    def stop_game(self):
        self.state = 99
    
    def render(self):
        pass