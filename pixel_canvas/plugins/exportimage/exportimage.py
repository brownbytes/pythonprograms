#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Export as image feature for Pixel Canvas

##########################################################################################

from libs.PygameButton import PygameButton
import pygame

hasTkGui = False
try:
    from Tkinter import Tk
    from tkFileDialog import asksaveasfilename
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    hasTkGui = True
except:
    pass
    
    
class ExportImage():    

    def __init__(self, margin, canvasside, pixieside, gap, canvas, noGrid=True):        
        self.MARGIN = margin
        self.CANVASSIDE = canvasside
        self.PIXIESIDE = pixieside
        self.GAP = gap
        self.canvas = canvas
        self.freeMarginY = self.canvas.freeMarginY
        x = self.CANVASSIDE - self.MARGIN + 10
        y = self.canvas.freeMarginY + 20
        # initialize interface buttons
        self.exportButton = PygameButton("export", x, y, w=60, h=20, onclick=self.export, canvasSurface=self.canvas.canvas)
        self.canvas.freeMarginY += 20 + 20
        self.noGrid = noGrid
            

    def export(self):
        # export canvas as image   
        filename = "pixel_canvas.png"                 
        try:
            if hasTkGui:
                filename = asksaveasfilename(defaultextension=".png", filetypes=[("PNG", ".png")], initialfile="pixel_canvas.png")
            print "Image exported!"
        except:
            print "Error in exporting image"
            return

        exportSurface = None       
        if self.noGrid:
            realPixieSide = self.PIXIESIDE + self.GAP 
            noGapCanvasW = self.PIXIESIDE * ((self.CANVASSIDE-self.MARGIN) / realPixieSide)
            noGapCanvasH = self.PIXIESIDE * (self.CANVASSIDE / realPixieSide)
            exportSurface = pygame.Surface((noGapCanvasW, noGapCanvasH))

            y, ys = 0, 0
            while y < noGapCanvasH:
                x, xs = 0, 0
                while x < noGapCanvasW:
                    pygame.draw.rect(exportSurface, self.canvas.canvas.get_at((xs, ys)), (x, y, self.PIXIESIDE, self.PIXIESIDE))
                    x += self.PIXIESIDE
                    xs += realPixieSide                
                y += self.PIXIESIDE
                ys += realPixieSide
        else:
            exportSurface = pygame.Surface((self.CANVASSIDE-self.MARGIN, self.CANVASSIDE))
            exportSurface.blit(self.canvas.canvas, (0,0))

        pygame.image.save(exportSurface, filename)

        
    def onMouseClick(self, eventObj):
        if (eventObj.pos[0] < self.CANVASSIDE - self.MARGIN or eventObj.pos[1] < self.freeMarginY):
            return
        self.exportButton.onMouseClick(eventObj)
    
    

