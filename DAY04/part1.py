import os

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Example.txt")).read().strip()
C = D.split('\n')
play = {}
for l in C:
  Cards = l.split(":")
  for Card in Cards:
    winnings = Card.split('|')

print(Cards)
print(winnings)