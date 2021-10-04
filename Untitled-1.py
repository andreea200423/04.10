n=int(input('Introduceti numarul de linii matrice: '))
a=[]
p=0
s=0
dps=0
dpj=0
ssp=0
sdp=0
if n>=2 and n<=10:
for x in range(n):
a.append([])
for x in a:
print('sir:',a.index(x)+1)
for j in range(n):
x.append(int(input('nuamrul: ')))
for z in range(0,len(a)):
p+= a[z][z]
print('a)suma pe diagonala principala: ',p)
s += a[len(a)-z-1][z]
print('b)suma pe diagonala secundara: ',s)
for x in range(n):
for z in range(n):
if x<z:
dps +=a[x][z]
print('dps)suma mai sus de diagonala principală este ', dps)
if x>z:
dpj+=a[x][z]
print('dpj)suma mai jos de diagonala principală este ', dpj)
if z+x<n-1:
ssp+=a[x][z]
print('ssp)suma mai stanga de diagonala principală este ', ssp)
if z+x>n-1:
sdp+=a[x][z]
print('sdp)suma mai dreapta de diagonala principală este ', sdp)
else:
print('erorrr')
