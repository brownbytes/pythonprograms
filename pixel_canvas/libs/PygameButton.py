#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Button class for pygame

##########################################################################################

import pygame
from pygame.locals import*

class PygameButton():
    self.rect = None
    self.normalButtonSurface = None       
    self.font = None 
    self.bgcolor = None
    self.fontcolor = None
    self.onClick = None

    def __init__( self, text, x=0, y=0, w=60, h=20, bgcolor=(255, 255, 255), fontcolor=(0, 0, 0), onclick = None):
        pygame.font.init()
        self.font = pygame.font.Font('Junction.ttf', 14)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text                
        self.onClick = onclick
        self.initButtonSurface()
        
    
    def initButtonSurface(self):
        self.normalButtonSurface = pygame.Surface(self.rect.size)
        self.normalButtonSurface.fill(self.bgcolor)
        textSurface = self.font.render(self.text, True, self.fontcolor, self.bgcolor)
        textRect = textSurface.get_rect()
        textRect.center = int(self.rect.width/2), int(self.rect.height/2)
        self.normalButtonSurface.blit(textSurface, textRect)
        
    def draw(self, canvasSurface):
        canvasSurface.blit(self.normalButtonSurface, self.rect)
        
    def onMouseClick(self, evenObj):
        if self.rect.collidepoint(eventObj.pos):
            self.onClick()
            