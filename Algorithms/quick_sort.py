'''
name :durga
program : quick -sort
quick sort involves partioning an input array around a pivot and
moving all values less than the pivot
to the right of the pivot and values greater than the pivot to the right of pivot.
these values withint themselves need not be ordered.
the total list is made up of three parts, 1 part is < pivot, second part is > pivot aand
thrid part is not yet worked upon.
i indicates the boundary between <p and >p
j indicates the boundary between partioned and unpartioned list
this program always moves the pivot as the first number of the list before sorting
for ex : 38251476 , if 3 is choosen as pivot ,
-----------------
|3|8|2|5|1|4|7|6|
  ^
  | i,j

-----------------  increment j as 8 is already > p 
|3|8|2|5|1|4|7|6|
  ^ ^
  |i|j

-----------------
|3|8|2|5|1|4|7|6|  => 2 < 3 , swap 8 and 2
  ^   ^
  |i  |j

-----------------
|3|2|8|5|1|4|7|6|  => increment i to represent the boundary between < and >. j is incremented as usual
    ^   ^
    |i  |j
-----------------
|3|2|8|5|1|4|7|6|  => 1 < 3 , swap 8 and 1 as 8 is the boundary for <p
    ^     ^
    |i    |j

-----------------
|3|2|1|5|8|4|7|6|  => 1 < 3 , increment i and j to reflect the same
      ^     ^
      |i    |j

'
'
'
-----------------
|3|2|1|5|8|4|7|6|  => since all the elements have been partioned, move pivot to its right position ie 'i'
      ^          ^
      |i         |j
    
one such above pass results on grouping of all the elements less than i (pivot) onto the left and all the elements greater than pivot to the right
the partioning is recusrivly run on the left list, chosing a new pivot and performing inline partioning, and creating another set of left and right lists. thus this continues till
there are no more partions left. the right list is also worked upon in the  same fashion creating child sets of left and right lists and partioning the elements around newly choosen pivot.

'''

import random


input_list = [8, 9, 6, 7, 10, 3, 2, 4, 1, 5]
#open a file or assign input_list
##fd = open('100num.txt','r')
##for line in fd:
##    input_list.append(int(line))

count = 0

  
def partioning(input_list,left,right):
  i = left # keeps track of '>' , '<' boundary , indicates the position of the pivot as well.
  j = left # keeps track of partitioned to unpartitioned boundary

  pivot_index = random.choice(range(i,len(input_list)))
  input_list[0],input_list[pivot_index]=input_list[pivot_index],input_list[0]
  
  temp = None
  
  for j in range(left,right+1):
    if j > left:
      if input_list[j] > input_list[0]:
        pass # do nothing just increment j as part of for loop
      elif input_list[j] < input_list[0]: # if value @ j is less than pivot , then swap the rightmost value of i with the j value
        input_list[i+1],input_list[j] = input_list[j],input_list[i+1]
        i +=1
  input_list[i],input_list[0] = input_list[0],input_list[i] # puttin pivot in its place after all the elements are partioned
  pivot_index = i

  return input_list,pivot_index


def quicksort(input_list):
  # pivot index is the boundary for diving and solving the quick sort
  # elements less than pivot are solved as one list, and elements greater than pivot are solved as second list.
  global count
  count += len(input_list)-1
  inplst,ind = partioning(input_list,0,len(input_list)-1)
  lftinplst = inplst[:ind]
  rgtinplst = inplst[ind+1:]

  if len(lftinplst) > 1:
    lftinplst = quicksort(lftinplst)

  if len(rgtinplst)> 1:
    rgtinplst = quicksort(rgtinplst)

  return lftinplst+[inplst[ind]]+rgtinplst


print quicksort(input_list)
print 'number of inversion:' + str(count)
