#st1 = raw_input('Enter a string, no delimiters: ')
#print st1
#for c  in st1: print ord(c),

#str = 'never odd or even'
#for c in reversed(str):
#    st1 += c
    
#st = 'Python\'s string class'
# index will crash it is just to mimic the index function for lists
#print st1.index('t', 5, 11)
#print st1.find('t')

q = 10

bin_rep = []
while q > 0 :
    bin_rep.append(q % 2)
    q = q / 2

bin_rep = bin_rep[::-1]
print bin_rep
