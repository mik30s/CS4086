#print "Python's string class"
#print 'Python\'s string class'

#print """Pythons's string class
#has many useful methods\n"""

st = 'abcd'
st = 'efgh'
#print st
st = st + 'ijk'

st1 = 'Michael'
st2 = 'Kwabena'
st3 = 'Osei'
st4 = st1 + ' ' + st2 + ' ' + st3
#print st4


#print st4[16:20] + ', ' + st4[0:7] + ' ' + st4[8:15]

st = ''
for c in st1:
    st += c + '-'
st = st[:len(st)-1]
print st
print chr(85)
