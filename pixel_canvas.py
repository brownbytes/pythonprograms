#usr/bin/env python
#author : durga
# the program is a pixel-canvas. clicking on a box colours the box black and double-clicking
#on the same box colours it back to white.
###########


import pygame,sys
from pygame.locals import *

#initialising variables

class PAINT(): #initialise a canvas, paint the boxes
	NAVYBLUE = (0,0,255)
	canvasside = 400
	blitpos = {}
	def __init__(self):
		self.canvas = pygame.display.set_mode((self.canvasside,self.canvasside))
		self.canvas.fill(self.NAVYBLUE)
		#pygame.display.update()
	def blit_pixiey(self,pixiey):
		row = 0
		col = 0
		margin = 2
		#check the number of pixiey screens which can fit on the canvas
		pixie_id = 0
		while col < self.canvasside:
			row = 0
			while row < self.canvasside:	
				self.canvas.blit(pixiey.pixie,(row,col))
				self.blitpos[pixie_id] = [row,col]
				row += (pixiey.pixieside+margin)
				pixie_id += 1
			col += (pixiey.pixieside+margin)
			
		
		
	def update_canvas(self):
		pygame.display.update()
	
	def get_color(self,posx,posy,pixie):
		canvaspixel = self.canvas.get_at((posx,posy))
		if canvaspixel == pixie.BLACK:
			return 'BLACK'
		elif canvaspixel == pixie.WHITE:
			return 'WHITE'
				


class PIXIE(): # each 10*10 box is called a pixie
	WHITE = (255,255,255)
	BLACK = (0,0,0) 
	pixieside  = 8

	def __init__(self):#intialising a surface known as 'pixie'
		self.pixie = pygame.Surface((self.pixieside,self.pixieside))
		self.pixie.fill(self.WHITE)

	def click(self,posx,posy,canvas):#click on a pixie fills the surface pixiey with black
		margin  = 2
		outerside = margin + self.pixieside
		for id in canvas.blitpos.keys():
			if (canvas.blitpos[id][0] <= posx < canvas.blitpos[id][0]+outerside) and (canvas.blitpos[id][1] <= posy < canvas.blitpos[id][1]+outerside):
				x = canvas.blitpos[id][0]
				y = canvas.blitpos[id][1]
		pygame.draw.rect(canvas.canvas,self.BLACK,(x,y,self.pixieside,self.pixieside))

	def unclick(self,posx,posy,canvas):
		margin  =2
		outerside = margin + self.pixieside
		for id in canvas.blitpos.keys():
			if (canvas.blitpos[id][0] <= posx < canvas.blitpos[id][0]+outerside) and (canvas.blitpos[id][1] <= posy < canvas.blitpos[id][1]+outerside):
				x = canvas.blitpos[id][0]
				y = canvas.blitpos[id][1]
		pygame.draw.rect(canvas.canvas,self.WHITE,(x,y,self.pixieside,self.pixieside))

def main():
	pygame.init()
	canvas = PAINT()
	pixiey = PIXIE()
	canvas.blit_pixiey(pixiey)
	
	while True:
		for event in pygame.event.get():
			if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				(mouse_x,mouse_y) = pygame.mouse.get_pos()
				COLOR = canvas.get_color(mouse_x,mouse_y,pixiey)
				if COLOR == 'WHITE':
					pixiey.click(mouse_x,mouse_y,canvas)
				elif COLOR == 'BLACK' :
					pixiey.unclick(mouse_x,mouse_y,canvas)
		canvas.update_canvas()

main()

