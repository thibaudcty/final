import pygame

class Camera:

    def __init__(self, width, height):
        
        self.width = width
        self.height = height

        self.scroll = pygame.Vector2(0,0)
        self.dx = 0
        self.dy = 0
        self.speed = 25     #the spped we can see the map with

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        #x
        if mouse_pos[0] > self.width *0.97 and mouse_pos[0] < self.width-1: #If the x value in the mouse pos is almost at the edge of the screen
            self.dx = -self.speed  
        elif mouse_pos[0] < self.width * 0.03 and mouse_pos[0] > 0:
            self.dx = self.speed
        else:
            self.dx = 0

        #Y
        if mouse_pos[1] > self.height *0.97 and mouse_pos[1] < self.height-1:
            self.dy = -self.speed  
        elif mouse_pos[1] < self.height * 0.03 and mouse_pos[1] > 0:
            self.dy = self.speed
        else:
            self.dy = 0  


        self.scroll.x += self.dx
        self.scroll.y += self.dy
            
