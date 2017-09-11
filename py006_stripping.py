st = ' foo '       # has 2 leading spaces and 5 trailing
print("|" + st + "|")

st1 = st.lstrip()     # left whitespaces are striped
print("|" + st1 + "|")

st2 = st.rstrip()     # right whitesapces are striped
print("|" + st2 + "|")

st3 = st.strip()
print("|" + st3 + "|")

#if you use strip with an argument. it will remove
#all the characters but not with white space.

st = '$%$^  foo    %^^^^'
st4 = st.strip('$%^')
print("|" + st4 + "|")

"""
Spliting and joining is also possible 
"""
# it wroks the same as strip. It will remove characters that are 
# not in the string
st = 'The quick brown fox jumps over the lazy dog'
print st.split()

st = 'The--quick--brown--fox-jumps--over--the--lazy--dog'
print st.split('--')

# combining split and strip
st = 'one  ;two;  three   ; four\t; five\n'
st1 = st.split(';')
for i,a in enumerate(st1):
    st1[i] = a.strip()
print st1

#you could also use string.splitlines