# this script is teaches how to open and read files
# r is optional
f = open("cities_distances.txt", 'r')

# there are several ways of reading a file

# eveytime you read something from a file it is also a 
# string

# read() will just read the data into a variable
data = f.read()
print data

# readlines() will read each line and place them into a list
# remember the file pointer must be reset if you want to continue 
# readiing from the file
print f.readlines()

# you must always close files as soon as you are 
# done
#f.close()

# or you can use 'with' statements
with open('cities_distances.txt', 'r') as f:
    li = f.read().split()
    for i,s in enumerate(li):
        li[i] = float(s)
    # do work here.
    ave = sum(li)/len(li)
    print ave
    
# or you could use readline

# to control the file cursor use seek and tell to 
# show where you are
# seek(0) takes the cursor to the beginning in the file
f = open('cities_distances.txt', 'r')
print f.readlines()
print f.tell()
f.seek(0)
print f.tell()
print 'Second time;'
print f.readlines()

# if you want to write to the file
# then use append
with open('cities_distances.txt', 'a') as f:
    pass

# write to new file use 'w' write
with open('cities_distances_1.txt', 'w') as f:
    f.write(data)

# write to new file use 'w' write
with open('cities_distances_1.txt', 'a') as f:
    f.write(data)
    
'''
 Write a script that stores 100 random integers in the range 24 – 42 
 in a file called hundred.txt. Each number should be on its own line. 
 It then reads the numbers back from the file, 
 adds them up, and writes the sum as the last element of the file. 
'''
from random import randint

with open('hundred.txt', 'w') as f:
    for i in range(100):
        n = randint(24,42)
        f.write(str(n) + '\n')    

s = 0
with open('hundred.txt', 'r') as f:
    for i in range(100):
        s += int(f.readline())
    print s
with open('hundred.txt', 'a') as f:
    f.write(str(s) + '\n')
    
'''
readlines and writelines
'''
li = None
with open('cities_distances.txt', 'r') as f:
    li = f.readlines()
with open('cities_distances.txt', 'w') as f:
    f.writelines(li)
    
    
    