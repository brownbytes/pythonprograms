#####merge sort algorithm ####
'''
name :durga
merge sort algorithm:

recursively break a given list till the list is tinest of size 1
sort the list and merge the 2 parts into 1 part.
arrive to breaking the initial list into two sorted parts by sorting and merging smaller lists

'''


count = 0
def sort_list(unsortedlist):

    m = len(unsortedlist)
# break the given list into 2 parts
    A_list = unsortedlist[:m/2] 
    B_list = unsortedlist[m/2:]

#perform recursive splitting of the first half till the lenght of the smallest leaf is 1
    if len(A_list) > 1: 
        A_list = sort_list(A_list)
       
#perform recursive splitting of the second half till the lenght of the smallest leaf is 1
    if len(B_list) > 1: # breaking and sorting second part
        B_list = sort_list(B_list)

# merge the smaller lists to return either a-list/b_list or full_list 
    return merge_sort(A_list,B_list)        

def merge_sort(a_list,b_list):

    temp_b = []
    initiallist = a_list+b_list
    final_list = []
    i = 0
    j = 0
    global count
    
    while len(final_list) < (len(initiallist)):
    #a_list is left part of the complete list and b_list is the right side. For ascending sequences,in the final result
    #elements in first half of list (a_list) are lesser than the second half of the list(b_list)
        
    # as long as a_list and b_list are not empty
        if len(a_list) != 0 and len(b_list) != 0:

            if  a_list[0] < b_list[0]:  # needs no swapping as a_list element is already lesser than b_list element
                final_list.append(a_list.pop(0))
                
            elif a_list[0] > b_list[0]: # needs swapping. Now, the count variable indicates how smaller is the b_list[0] 
            #since b_list[0] is being before all the a_list list items, it turns out we are comparing b_list[0] to all the items from a_list
                item = b_list.pop(0)
                final_list.append(item)
                count += len(a_list)                        

            elif a_list[0] == b_list[0]:
                final_list.append(a_list[0])
                final_list.append(b_list[0])
                

        elif len(b_list) == 0:
            final_list += a_list        
            

        elif len(a_list) == 0 :
            final_list+=b_list


    print count, a_list,b_list
        
    return final_list



