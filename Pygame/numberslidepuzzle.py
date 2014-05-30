# version1 -slide_game_v1.py  of game blits numbers on diff tile surfaces, then blits the tiles on the canvas. 
#the current v2 of the game, checks if a slot on the canvas is vacant or not. 
#initially all the positions where the tiles will be blitted are made vacant, and made false when a tile is blitted. 
#Thus at the start of game 1, slot is always vacant.
# ver 2.0 completes the game play but doesnot include game completion verification. v3 includes game completion verification and restarting a new game 
#!usr/bin/env python

import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.font.init

BGCOLOR = (0,128,225)
#TILECOLOR = (128,255,255)
WHITE =(255,255,255)
BLACK = (0,0,0)
#tile colours
COLORDICT = {'AQUA':(0,255,255),
'FUSHSIA':(255,0,255),
'GRAY':(128,128,128),
'LIME':(0,255,0),
'MAROON':(128,0,0),
'NAVYBLUE':(0,0,128),
'OLIVE':(128,128,0),
'PURPLE':(128,0,128),
'SILVER':(192,192,192),
'TEAL':(0,128,128),
'YELLOW':(255,255,0),
'LIGHTBLUE':(128,255,255),
'RED':(255,0,0),
'GREEN':(0,128,0),
'WHITE':(255,255,255)}


TEXTCOLOR = (255,255,255)
GAP = 1
CANVASSIDE = 403
TILESIDE = 60
MARGIN = 80

global isvacant
isvacant = {}
global isgameover
isgameover = False
global slotnum
slotnum = {}
global tileseq
tileseq = {}
global tileposi
tileposi = {}

#helper functions#
def tileposition():
# to determine tile position
	global isvacant
	global slotnum
	tilepos =[]
	i = 0
	for posy in range(MARGIN,CANVASSIDE-MARGIN,TILESIDE+GAP):
		posx = 0
		for posx in range(MARGIN,CANVASSIDE-MARGIN,TILESIDE+GAP):
			tilepos.append((posx,posy))
	for slot in tilepos:
		isvacant[slot] = True
		slotnum[slot] = i
		i +=1
	return tilepos

def vacantslot(posx,posy):

#posx,posy are mouse clicks, if there is a vacant slop around the tile, the tile can be moved into that slot.

#checking if adjcent slot is empty
	for pos in isvacant.keys():
		if ((pos[0] <= posx <= pos[0]+TILESIDE+GAP) and (pos[1] <= posy <= pos[1]+TILESIDE+GAP)):
			slotx = pos[0]
			sloty = pos[1]

	if ((slotx+TILESIDE+GAP,sloty) in isvacant.keys()) and (isvacant[(slotx+TILESIDE+GAP,sloty)]) == True:
		return 'right',(slotx,sloty)

	elif ((slotx-(TILESIDE+GAP),sloty) in isvacant.keys()) and (isvacant[(slotx-(TILESIDE+GAP),sloty)]) == True:
		return 'left',(slotx,sloty)
	
	elif ((slotx,sloty+TILESIDE+GAP) in isvacant.keys()) and isvacant[(slotx,sloty+TILESIDE+GAP)] == True:
		return 'bottom',(slotx,sloty)

	elif ((slotx,sloty-(TILESIDE+GAP)) in isvacant.keys()) and isvacant[(slotx,sloty-(TILESIDE+GAP))] == True:
		return 'top',(slotx,sloty)
	else:
		return None

def movetile(direction,slot):
#based on the vacant slot, the tile new coordinates are determined as below
	if direction == 'bottom':
		return ((slot[0],slot[1]+TILESIDE+GAP))
	elif direction == 'top':
		return ((slot[0],slot[1]-(TILESIDE+GAP)))
	elif direction == 'left':
		return ((slot[0]-(TILESIDE+GAP),slot[1]))
	elif direction == 'right':
		return ((slot[0]+TILESIDE+GAP,slot[1]))
	else:
		pass
	
emptytile = pygame.Surface((TILESIDE,TILESIDE))
emptytile.fill(BGCOLOR)

def checkgameover():
#the func checks for all the tile values to be true, any one false encountred will exit the cal

	for atile in tileposi.keys():
		if slotnum[tileposi[atile]] == tileseq[atile]:
			continue
		else:
			return False
			
			
	return True
	

class CANVAS():

	canvas = pygame.display.set_mode((CANVASSIDE,CANVASSIDE))
	
	def __init__(self):
		self.canvas.fill(BGCOLOR)
		
	def drawtiles(self,tile):
	#drawing the tiles on canvas	
		temptpdict = tile.tileposdict()
		for atile in temptpdict.keys():
			self.canvas.blit(atile,temptpdict[atile])
			isvacant[temptpdict[atile]] = False

	def updatecanvas(self,newtilepos):
		temptpdict = newtilepos
		for pos in isvacant.keys():
			if isvacant[pos] == False:
				for atile in temptpdict.keys():
					if temptpdict[atile] == pos:
						self.canvas.blit(atile,pos)
			elif isvacant[pos] == True:
				self.canvas.blit(emptytile,pos)
		pygame.display.update()

class TILE():
	def __init__(self,canvas,tilepos,colordict):
		self.canvas = canvas.canvas
		self.tilepos = tilepos
		self.tile = pygame.Surface((TILESIDE,TILESIDE))
		self.colordict = colordict
		self.tpdict = {}#tiles with numbers blitted at resp positions in tiles and position of tiles on the canvas

	def tileposdict(self):
	#assiging a position to a tile, when key is same name, dir is updated and not appended.
		global tileposi
		tilelist = self.drawNum() #tiles with numbers associated with them
		for i in range(len(tilelist)):
			self.tpdict[tilelist[i]] = self.tilepos[i]
			tileposi[tilelist[i]] = self.tilepos[i]
		return self.tpdict

	def slideanimation(self,posx,posy):
		global isvacant
	#sliding the tile to a vacant spot
		direction,slot = vacantslot(posx,posy)
		newpos = movetile(direction,slot)
		
		for atile in (self.tpdict.keys()):
			if self.tpdict[atile] == slot:
				self.tpdict[atile] = newpos
				isvacant[slot] = True
				isvacant[newpos] = False
				return self.tpdict
	

	def listoftiles(self):
	#making a dir of 15 tiles with indexes seems appending the same surface. Need to declare 15 different surfaces
		tilelist = [pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE)),
pygame.Surface((TILESIDE,TILESIDE)),pygame.Surface((TILESIDE,TILESIDE))]
		for i in range(len(tilelist)):
			tilelist[i].fill(self.colordict.values()[i])
		return tilelist

	def drawNum(self):
	# returns a list of tiles with numbers on them.each tile is tilelist is blit with number 
		global tileseq
		tilelist = self.listoftiles()
		fontObj = pygame.font.Font('freesansbold.ttf',30)
		textObj=[]
		
		NUMS = range(1,16)
		random.shuffle(NUMS)
		for i in range(len(NUMS)):
			textObj.append(fontObj.render(str(NUMS[i]),True,(0,0,0)))
			tilelist[i].blit(textObj[i],(TILESIDE/4,TILESIDE/4))
			tileseq[tilelist[i]]=NUMS[i]

		return tilelist

def main():
	pygame.init()
	pygame.font.init
	tilepos = tileposition()
	canvas = CANVAS()
	tile = TILE(canvas,tilepos,COLORDICT)
	canvas.drawtiles(tile)


	while isgameover == False:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEBUTTONUP:
				mousex,mousey = event.pos
				newtilepos =tile.slideanimation(mousex,mousey)
				canvas.updatecanvas(newtilepos)
			else:
				pass
		if checkgameover():
			pygame.quit()
			sys.exit()

		pygame.display.update()

main()
