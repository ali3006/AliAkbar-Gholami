S = input('Ent. Sth. : ')
S1 = S.split()
S2 = dict()
for i in S1:
    if i not in S2.keys():
        S2[i] = 0
    S2[i] = S2[i] + 1
print(S2)        
y = '((Ali Akbar Gholami))'
z = y.center(67,'0')
print(z)