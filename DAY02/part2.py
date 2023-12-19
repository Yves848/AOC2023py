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

Games = {}
sum = 0
i = 0
for G in L:
  i += 1
  game,balls = G.split(":")
  Games[game]=balls.split(";")
  print(game)
  minimums = {"red": 0, "green":0, "blue":0}
  for ball in Games[game]:
    print(ball)
    for b in ball.split(','):
      nb,color = b.strip().split(' ')
      if minimums[color] < int(nb):
        minimums[color] = int(nb)
  r = 1
  for n in minimums:
    r = r * minimums[n]
  sum += r

print(sum)