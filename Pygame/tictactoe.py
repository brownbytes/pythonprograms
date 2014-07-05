#########################
# author :durga
# date :25 june 2014
# TICTACTOE implementation using Monte Carlo Method.
# Coursera instructions
#########################

import random
from copy import deepcopy

class TTTBoard:
  """class to represent a tic-tac-toe board
  """

  def __init__(self,dimensions,reverse=False,board=None):
    """
    initialise the TTTBoard object with given dimensions and whether or
    not the game should be revered
    """
    #self.oriboard = []
    self.dim = dimensions
    self.players = ['_','X','O']

    if board == None: # for new game create new board
##      for _ in range(self.dim):
##        eachrow = []
##        for _ in range(self.dim):
##          eachrow.append('_')
##        self.oriboard.append(eachrow)
      self.oriboard = [['_' for dummycol in range(self.dim)]for dummyrow in range(self.dim)]
        

    elif board != None: #clone a board
##      for row in range(self.dim):
##        for col in range(self.dim):
##          self.oriboard[row][col] = board[row][col]
      self.oriboard = [[board[row][col] for col in range(self.dim)] for row in range(self.dim)]

  def __str__(self):
    """human readable representation of the board"""
    for cells in self.oriboard: #oriboard
      boardstr=''
      for each_cell in cells:
        boardstr +=  '_'+each_cell+'_' + '|'
      print '   '+'|'+'   '+'|'+'   '

      print boardstr[:-1] #remove tht extra ending'|'

    return '' # not returning anything

      #_(0, 0)_|_(0, 1)_|_(0, 2)_
      #_(1, 0)_|_(1, 1)_|_(1, 2)_
      #_(2, 0)_|_(2, 1)_|_(2, 2)_
  def get_dim(self):
    return self.dim

  def square(self,row,col):
    """returns the status (EMPTY,PLAYERX,PLAYERO) of the square at"""
    if self.oriboard[row][col] == '_':
      return 'EMPTY'
    elif self.oriboard[row][col] == 'X':
      return 'X'
    elif self.oriboard[row][col] == 'O':
      return 'O'

#print TTTBoard(3)
#print TTTBoard(3).square(2,1)

  def get_empty_squares(self):
    """return a list of (row,col) tuples for all empty squares"""
    empty_spaces = []
    for row in range(self.dim):
      for col in range(self.dim):
        if self.oriboard[row][col] == '_':
          empty_spaces.append((row,col))
    return empty_spaces

#print TTTBoard(3).get_empty_squares()

  def move(self,row,col,player):
    """place player on the board at a postion (row,col)"""
    self.oriboard[row][col] = player
    return self.oriboard


  def check_win(self):
    """
      If someone has won, return player.
      If game is a draw, return DRAW.
      If game is in progress, return None.
    """
    '''winning = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
               [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    '''
    winning = [[self.square(0,0),self.square(0,1),self.square(0,2)],
               [self.square(1,0),self.square(1,1),self.square(1,2)],
               [self.square(2,0),self.square(2,1),self.square(2,2)],
               [self.square(0,0),self.square(1,0),self.square(2,0)],
               [self.square(0,1),self.square(1,1),self.square(2,1)],
               [self.square(0,2),self.square(1,2),self.square(2,2)],
               [self.square(0,0),self.square(1,1),self.square(2,2)],
               [self.square(0,2),self.square(1,1),self.square(2,0)]]
  
    #print winning   

    if ['X','X','X'] in winning:
      return 'X'

    elif ['O','O','O'] in winning:
      winner = 'O'
      return 'O'

    elif len(self.get_empty_squares()) == 0 and (not(['X','X','X'] in winning or ['O','O','O'] in winning)):
      return 'DRAW'

    #elif len(self.get_empty_squares()) > 0: # game in progress
     # return None
    

  def switch_player(self,player):
    if player == 'X':
      return 'O'
    elif player == 'O':
      return 'X'
        

  def clone(self):
    """ returns a copy of the board"""
    #self.cloneboard = deepcopy(self)
    return TTTBoard(self.dim,reverse=False,board=self.oriboard)

# to calculate AI move

NTRIALS = 100 #number of trials to run
MCMATCH = 1.0 #score for squares played by the machine
MCOTHER = 1.0 #score for squares played by the other player

def mc_trial(board,player):
  """ randomly playes the board once,alters cloned board, doesnot return"""
  temp_player = player
  emptycells = board.get_empty_squares()

  while board.check_win() == None:
    nextcell = random.choice(emptycells)
    board.move(nextcell[0],nextcell[1],temp_player)
    temp_player = board.switch_player(temp_player)
    emptycells = board.get_empty_squares()

  return 

def mc_update_scores(scores,board,player):
  """scores the clone board played during mc_trial"""
  winner = board.check_win()

  if winner == 'X':
    opl = 'O'
  elif winner == 'O':
    opl = 'X'
    
  dim = board.get_dim()
  
  if winner in ['X','O']: #if machine won,
    for row in range(dim):
      for col in range(dim):
        if board.square(row,col) == winner:
          scores[row][col] += 1.0
        elif board.square(row,col) == 'EMPTY':
          scores[row][col] += 0.0
        elif board.square(row,col) == opl: #mark all human blocks
          scores[row][col] -= 1.0
          
  elif winner == "DRAW": # if a draw
    for row in range(dim):
      for col in range(dim):
        scores[row][col] += 0.0
        

def get_best_move(board,scores):
  """finds all empty spaces with max score and returns a cell """
  emptycells = board.get_empty_squares()
  maxscorelist = []
  mx = []

  for cell in emptycells:
    maxscorelist.append(scores[cell[0]][cell[1]])
  maxvalue = max(maxscorelist)
                        
  for (row,col) in board.get_empty_squares():
    if scores[row][col] == maxvalue:
      return (row,col)


def mc_move(board,player,trials):
  """simulation of monte carlo method to calculate best cell"""

  scorelist= [] #score[row][col]

  for _ in range(board.get_dim()):
    rowlist = []
    for _ in range(board.get_dim()):
      rowlist.append(0.0)
    scorelist.append(rowlist)

  for _ in range(trials):
    cb = board.clone()
    mc_trial(cb,player)
    mc_update_scores(scorelist,cb,player)
    #print scorelist

  
  return get_best_move(board,scorelist)
  
def play_game(func,trials,reverse):

  oriboard = TTTBoard(3)
  print " board coords"
  print "(0, 0)|(0, 1)|(0, 2)"
  print "______|______|______"
  print "(1, 0)|(1, 1)|(1, 2)"
  print "______|______|______"
  print "(2, 0)|(2, 1)|(2, 2)"
  print "______|______|______"
  
  pl = 'X'
  i = 1
  winner = None
  while winner == None:
    pos = func(oriboard,pl,trials)
    oriboard.move(pos[0],pos[1],pl)
    print oriboard
    winner = oriboard.check_win()
    if winner:
      break
    print "please enter coords you want to play (x,y)"
    usercords = input("cords:")
    if usercords not in oriboard.get_empty_squares():
      print "invalid"
      usercords = input("cords:")
    pl = oriboard.switch_player(pl)
    oriboard.move(usercords[0],usercords[1],pl)
    
    pl = oriboard.switch_player(pl)
    winner = oriboard.check_win()
    print oriboard    
    i += 1

  if winner  == 'X':
    print 'X'
  elif winner == 'O':
    print 'O'
  elif winner == 'DRAW':
    print "Tie!"
  else:
    print "unknown"


play_game(mc_move, NTRIALS, False)

