from math import sqrt, ceil

li = []
LIST_SIZE = 400
for i in range(LIST_SIZE):
    li.append(sqrt(i))

hist = [0] * int(ceil(max(li)))
print "no. of bins: ",len(hist)
for i in range(LIST_SIZE):
    hist[int(li[i])] += 1
    print hist
    
 