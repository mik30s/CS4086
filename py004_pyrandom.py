from random import random, randint, uniform

#li = []
#for i in range(15):
#    li.append((random() * 16) + 5)
#print li
    
#li = []
#for i in range(15):
#    li.append(uniform(5, 16))
#print li
    
#li = []
#for i in range(100):
#    li.append(randint(0,14) * 7)
#print li

# tuples
#tu = ('abcd', 42, 3.3, 100L, [1,2,3],(1,2,3))
#print tu

#li = [()] * 10
#print li
#f_sum=0
#s_sum=0
#for i in range(len(li)):
#    li[i] = (random(), random())
#    f_sum += li[i][0]
#    s_sum += li[i][1] 
#print f_sum, s_sum
f_sum = 0
s_sum = 0
print zip(*([(random(), random())] * 1000))
