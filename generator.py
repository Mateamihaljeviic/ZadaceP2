'''
Napraviti generator funkcije za ispis svih parnih i svih
neparnih brojeva manjih od prosljeđenog parametra.
'''

import random

def parni(broj):
    for b in range(broj):
        if b%2==0:
            yield b

def neparni(broj):
    for b in range(broj):
        if b%2!=0:
            yield b

broj=random.randint(0, 100)
print(broj)

print("Parni: ", list(parni(broj)))
print("Neparni: ", list(neparni(broj)))
