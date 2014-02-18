#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Button class for pygame

##########################################################################################

import pygame
from pygame.locals import*
import os

# the current directory is by default from where the code runs
# change it to current directory of this file for proper resource file laoding
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class PygameButton():    

    def __init__(self, text, x=0, y=0, w=60, h=20, bgcolor=(255, 255, 255), fontcolor=(0, 0, 0), onclick = None, canvasSurface = None):        
        self.normalButtonSurface = None         
        self.bgcolor = bgcolor
        self.fontcolor = fontcolor        
        pygame.font.init()
        self.font = pygame.font.Font('Junction.ttf', 14)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text                
        self.onClick = onclick
        self.canvasSurface = canvasSurface
        self.initButtonSurface()
        self.draw(self.canvasSurface)
        
    
    def initButtonSurface(self):
        self.normalButtonSurface = pygame.Surface(self.rect.size)
        self.normalButtonSurface.fill(self.bgcolor)
        textSurface = self.font.render(self.text, True, self.fontcolor, self.bgcolor)
        textRect = textSurface.get_rect()
        textRect.center = int(self.rect.width/2), int(self.rect.height/2)
        self.normalButtonSurface.blit(textSurface, textRect)
        
    def draw(self, canvasSurface):
        canvasSurface.blit(self.normalButtonSurface, self.rect)
        
    def onMouseClick(self, eventObj):
        if self.rect.collidepoint(eventObj.pos):
            print self.text, "button clicked"
            self.onClick()
            