
# author :durga


numdict = {}
count = 0

with open('2sum.txt') as fd:
    for integer in fd:
        numdict[int(integer)] = int(integer)

print "numdict computed"

for t in range(-10000,10001):
    
    for num in numdict:
        if t-num in numdict:
            count += 1
            break

print '2.computed numdict'
   

print 'done'
print count
