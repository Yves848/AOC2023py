import sys
import os
from pathlib import Path
import re

print(sys.argv[0])
#D = open(sys.argv[1]).read().strip()
file = os.path.dirname(__file__)

print(file)
D = open(os.path.join(file,"Data.txt")).read().strip()
L = D.split("\n")

possibles = {"red": 12, "green": 13, "blue":14}

Games = {}
sum = 0
i = 0
for G in L:
  i += 1
  game,balls = G.split(":")
  Games[game]=balls.split(";")
  print(game)
  possible = True
  for ball in Games[game]:
    print(ball)
    for b in ball.split(','):
      pair = b.strip().split(' ')
      if int(pair[0]) > possibles[pair[1]]:
        print(game+" not possible")
        possible = False
        break
  if possible:
      sum += i



print(sum)  