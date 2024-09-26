'''
Napisati program koji generira kvadratnu matricu dimenzija 5x5.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na glavnoj dijagonali matrice.
(glavna dijagonala ide od gornjeg lijevog u donji desni kut matrice).
'''
import random

r = 5
s = 5
zbroj = 0

matrica = []

for i in range(r):
    red = [0]* s
    matrica.append(red)
    for j in range(s):
        nasumicni = random.randint(1,10)
        matrica[i][j] = nasumicni
        
print("Matrica 5x5")

for i in matrica:
    print(i)


for i in range(len(matrica)):
    zbroj += matrica[i][i]

print("Zbroj na glavnoj dijagonali:", zbroj)
print(" ")

'''
Zadaća
Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.
'''
import random

r = 7
s = 7
zbroj = 0

matrica = []

for i in range(r):
    red = [0]* s
    matrica.append(red)
    for j in range(s):
        nasumicni = random.randint(1,10)
        matrica[i][j] = nasumicni

dimenzija = len(matrica)
for i in range(dimenzija):
    zbroj += matrica[0][i]  
    zbroj += matrica[dimenzija-1][i] 
    if i != 0 and i != dimenzija - 1:
        zbroj += matrica[i][0] 
        zbroj += matrica[i][dimenzija-1]
        
print("Matrica 7x7")

for i in matrica:
    print(i)

print("Zbroj elemenata na rubovima matrice:", zbroj)
