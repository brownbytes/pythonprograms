__author__ = 'vijayadurga'
""" read a file of movie names
     selects a movie from 2 languages :hindi, english
     difficulty level of easy, medium, hard
     english = {'easy':{1:'ab',2:'xy'...},'medium':{1:'ab',2:'xy'...},'hard':{1:'ab',2:'xy'...}}
     hindi = {'easy':{1:'ab',2:'xy'...},'medium':{1:'ab',2:'xy'...},'hard':{1:'ab',2:'xy'...}}
"""

"""
if a spefici movie catoery such as hindi easy, eng easy doesnot exist the random
cchoice module returns index error on runnning on empty list

to fix:
movie repetitions
timer
background color for eng and hind
enter key inclusion
"""

import random
import urllib
import csv
import pygame
import sys
from pygame.locals import *
#from csv import DictReader,DictWriter

used_up=[None]
LANG = set([])
DIFF = set([])
flag = 0


def readFile():
    """
    input: read url or from csv file
    output: a dict with all movie names stored in dict
    """
    movie_dict = {'HIN':{'HARD':{},'MED':{},'EASY':{}},'ENG':{'HARD':{},'MED':{},'EASY':{}}}

    global LANG
    global DIFF
    
    with open('movies1.csv','rU') as moviefile:
        movies = csv.reader(moviefile)
        i = 0
        j = 0
        for movie in movies:
            LANG.add(movie[0])
            DIFF.add(movie[1])
            if movie[0] == "HIN":
                movie_dict[movie[0]][movie[1]][i] = movie[2:]
                i += 1
            elif movie[0] == 'ENG':
                movie_dict[movie[0]][movie[1]][j] = movie[2:]
                j += 1

    return movie_dict


def suggestMovie(movie_file):

    """
     input : a file with all movie names
     output : movie

    """
    global used_up
    specs = chooseLang()
    try:
        seed = random.choice(movie_file[specs[0]][specs[1]].keys()) # keep creating new seed if the movie is already chosen
    except:
        suggestMovie(movie_file)
        
    movie = movie_file[specs[0]][specs[1]][seed]
    return movie

def chooseLang():
    """
    input : numbers
    output : (language, difficulty)
    """
 #   LANG = ['ENG','HIN']
   # DIFF = ['HARD','HARD','HARD','MED','MED','MED','MED','MED','EASY','EASY']

    lang = random.choice(list(LANG))
    diff = random.choice(list(DIFF))

    return lang,diff
#
#md = readFile()

next_movie_but_rect=None
new_movie_display = None

class Window():

    next_movie_but  = None
    next_new_movie = None

    def __init__(self):
        """
        intialise a gui and listens to the new_movie button event

        """
        self.new_window = pygame.display.set_mode((900,500))
        self.new_window.fill((255,255,255))
        self.next_movieButton()
        self.renderNext_movie()

    def next_movieButton(self):
        """
         drawing the next_movie button
        """
        global next_movie_but_rect

        next_movie_but_rect = pygame.Rect((60,15),(50,50))
        pygame.draw.rect(self.new_window,(192,192,192),next_movie_but_rect,0)
        
        font = pygame.font.match_font('couriernew',bold=True,italic=False)
        font1 = pygame.font.Font(font,20) #next_movie button

        next_movie_but = font1.render('next_movie',1,(0,0,0),(192,192,192))
        self.new_window.blit(next_movie_but,(60,15))


    def renderNext_movie(self):
        """
        constantly updates the next movie display rectangle when the next_movie button is clicked
        """
        global new_movie_display,used_up,flag# checks for recursion
        
        movie_file = readFile()
        new_movie = suggestMovie(movie_file)[0]

        if new_movie in used_up:#recurively call for unique movie            
            if flag > 10:
                used_up=[]#reset used up
            else:              
                self.renderNext_movie()
                flag += 1
        

        used_up.append(new_movie)

        new_movie_display = pygame.Rect((60,50),(800,400))
        pygame.draw.rect(self.new_window,(192,192,192),new_movie_display,0)
        
        font = pygame.font.match_font('couriernew',bold=True,italic=False)
        font2 = pygame.font.Font(font,30)
        
        next_new_movie = font2.render(new_movie,1,(0,0,0),(192,192,192))
        self.new_window.blit(next_new_movie,(60,50)) #render next movie
       
        self.update_window()   

    def update_window(self):
        """
        updates window
        """
        pygame.display.update()

    def reset_timer(self):
        """
        timer

        """
        pass


def main():
    """
    main event handler

    """
    pygame.init()
    window = Window()
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            elif (event.type == MOUSEBUTTONDOWN or (event.type == pygame.KEYUP and pygame.key.name == 'K_RETURN')):
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                if next_movie_but_rect.collidepoint(mouse_x,mouse_y):
                    window.renderNext_movie()
                
        window.update_window()


main()
from pygame import font


