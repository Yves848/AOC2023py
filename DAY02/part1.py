import sys
import re

#D = open(sys.argv[1]).read().strip()
D = open("Example.txt").read().strip()
L = D.split("\n")

possibles = {"red": 12, "green": 13, "blue":14}

Games = {}
sum = 0

for G in L:
  game,balls = G.split(":")
  Games[game]=balls.split(";")
  for ball in Games[game]:
    for b in ball.split(','):
      pair = b.split(' ')
      if pair[0] > possibles[pair[1]]:
        print(game+" not possible")
        break
  