String = input(' A String:')
x = dict()
for i in String:
    if i in x :
        x[i] = x[i] + 1
    else:
         x[i] = 1
print( 'the times of its char.: ', x)
y = '((Ali Akbar Gholami))'
z = y.center(67,'0')
print(z)

