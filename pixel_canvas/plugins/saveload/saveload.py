#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Save and Load features for Pixel Canvas, in custom data format

##########################################################################################

class SaveLoad():
    self.MARGIN = 100
    self.CANVASSIDE = 700
    self.PIXIESIDE = 10
    self.GAP = 2
    self.canvas = None

    def SaveLoad(self, margin, canvasside, pixieside, gap, canvas):
        self.MARGIN = margin
        self.CANVASSIDE = canvasside
        self.PIXIESIDE = pixieside
        self.GAP = gap
        self.canvas = canvas

    def init(self):
        # initialize interface buttons
        pass

    def save(self, filename):
        # save in custom format
        '''
        Text file:
        --------------------------------------
        <savefile identifier>
        <canvas attributes>
        <color arrays, space separated>
        '''
        pass

    def load(self, filename):
        # load file and draw on canvas
        pass

