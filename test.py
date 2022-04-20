key = 'HELLOPYTHON'
string = 'GONE WITH THE WIND'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
set_key = set(key)
list_letter = set(letter)
code = list(list_letter-set_key)
code.sort()
lt_key=list(set_key)
lt_key.sort(key=key.index)
new_letter=lt_key+code
new_string=''
for i in string:
    if i==' ':
        new_string+=' '
    else:
        s=letter.index(i)
        new_string+=new_letter[s]
print (new_string)