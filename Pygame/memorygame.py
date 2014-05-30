## author :durga
##memory game 6*5

#!usr/bin/env python

import pygame
import sys
import random
import os
from pygame.locals import *

def reload():
	global DIRLISTING
	global IMGSIZE
	global margin
	global CANVASWIDTH
	global CANVASHEIGHT
	global REARSIDE
	global canvas
	global carddeck
	print "in reload"
	DIRLISTING = os.listdir('/Users/vijayadurga/Desktop/python/programs/IWPPYGAME/chap3/tobeused')
	random.shuffle(DIRLISTING)
	IMGSIZE= 64
	margin = 5
	CANVASWIDTH = 414 #cardsinarow * (imgsize+margin)
	CANVASHEIGHT = 345 #cardsinacol * (imgsize+margin)
	REARSIDE  =pygame.image.load('brown.png')	
	canvas = new_board()
	carddeck = card()
	
def game_over(cards,canvas):

	pygame.font.init()
	fontobj = pygame.font.Font('freesansbold.ttf',18)
	textobj = fontobj.render('GAMEOVER!!to cont hit "y"', True,(0,255,0))
	if False in cards.IMGDICT.values():
		return True
	elif False not in cards.IMGDICT.values():
		pygame.draw.rect(canvas.CANVAS,(0,0,0),(75,100,250,100))
		canvas.CANVAS.blit(textobj,(100,120))
		pygame.display.update()
		pygame.time.wait(10000)
		for event in pygame.event.get():
			if ((event.type == KEYDOWN or event.type == KEYUP) and event.key == 121):
				return 'newgame'
			elif ((event.type == KEYDOWN or event.type == KEYUP)and event.key == K_n):
				return False
			else:
				return False	

# Board class
class new_board():
	WHITE = (255,255,255)
	BLACK = (0,0,0)

	def __init__(self):
		self.CANVAS = pygame.display.set_mode((CANVASWIDTH,CANVASHEIGHT))
		self.CANVAS.fill(self.WHITE)
		pygame.display.update()

	def update_board(self,cards):
	#update the board to display cards based on their exposed state. if false display backside, it explist is true display the image
		
		for img in cards.IMGLIST:
			if cards.IMGDICT[img] == True:
				self.CANVAS.blit(img,cards.IMGPOSDICT[img])
				
			elif cards.IMGDICT[img] == False:
				self.CANVAS.blit(REARSIDE,cards.IMGPOSDICT[img])
				
		pygame.display.update()
	
	def compare_cards(self,card1,card2):
	#pixel comparision of two cards
		card1pxl = pygame.PixelArray(card1)
		card2pxl = pygame.PixelArray(card2)

		for row in range(50):
			for col in range(50):
				if card1pxl[row][col] == card2pxl[row][col]:
					continue
				else:
					
					return False
		return True


# card class
class card():
	explist =[] # this list stores the state of the board. if 2 cards are exposed, comparision triggers

	def __init__(self):
		self.IMGLIST = []#list of all images
		self.IMGDICT = {} #image to exposed mapping. if exposed and matched keep exposed
		self.IMGPOSDICT = {}#card and position mapping
		self.cardsinrow = 6
		self.cardsincol = 5
		j =0
		for i in DIRLISTING:#for loading 15 images twice from folder
			if '.png' in i and 'brown' not in i:#only png and none brown cards
				self.IMGLIST.append(pygame.image.load(i))#2 copies
				self.IMGLIST.append(pygame.image.load(i))
			if len(self.IMGLIST) >= 30:
				break

		random.shuffle(self.IMGLIST)
		random.shuffle(self.IMGLIST)
		
		#determing the positions of cards and updating card-position in IMGPOSDICT
		for imgposy in range(0,CANVASHEIGHT,(IMGSIZE+margin)):
			imgposx = 0
			for j in range(j,self.cardsinrow):
				self.IMGDICT[self.IMGLIST[j]] = False
				self.IMGPOSDICT[self.IMGLIST[j]] = (imgposx,imgposy)
				imgposx += (IMGSIZE+margin)
			if self.cardsinrow < len(self.IMGLIST):
				j = self.cardsinrow
				self.cardsinrow += 6 #moving to next row
		

	def display_card(self,mouse_x,mouse_y):
		#check for mouse click position, display respectie card and update explist[]
		for img in self.IMGLIST:
			if (((self.IMGPOSDICT[img][0]) < mouse_x < (self.IMGPOSDICT[img][0]+IMGSIZE)) and ((self.IMGPOSDICT[img][1]) <mouse_y < (self.IMGPOSDICT[img][1]+IMGSIZE))) and self.IMGDICT[img] == False:
				self.IMGDICT[img] = True
				if len(self.explist) < 2:
					self.explist.append(img)
				elif len(self.explist) >= 2:
					self.explist = []
					self.explist.append(img)
			
	def flip_card(self,canvas):
		# to compare the two cards in the explist , if they match - keep them exposed,else turn them over by setting IMGDICT back to false
		if len(self.explist) == 2:
			if canvas.compare_cards(self.explist[0],self.explist[1]):
				self.IMGDICT[self.explist[0]] = True
				self.IMGDICT[self.explist[1]] = True
			else:
				self.IMGDICT[self.explist[0]] = False
				self.IMGDICT[self.explist[1]] = False	

#start the pygame and the finite while loop to check


def main():
	
	reload()
	pygame.init()
	gamestatus = ''
		
	while True:
	
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONUP:
				mousex,mousey = event.pos
				carddeck.display_card(mousex,mousey)

		canvas.update_board(carddeck)
		carddeck.flip_card(canvas)
		pygame.time.wait(250)
		canvas.update_board(carddeck)
		gamestatus = game_over(carddeck,canvas)

		if gamestatus == True:
			continue
		elif gamestatus =='newgame':
			reload()
			continue
		else:

			break
			
main()
