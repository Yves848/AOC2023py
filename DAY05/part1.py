import os
import sys
import math

os.system('cls')

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Data.txt")).read().strip()
C = D.split('\n\n')

# print(C)

seeds = []
for c in (C[0].strip().split(":"))[1].strip().split(" "):
  seeds.append(int(c))

# print(seeds)

maps = []
i = 1
while i < len(C):
  map = C[i].strip().split('\n')
  # print(map)
  j = 1
  maps2 = []
  while j < len(map):
    maps2.append(map[j])
    j+=1
  maps.append(maps2)
  i+=1

lowest = sys.maxsize

for seed in seeds:
  print(f"seed {seed}")
  s=seed
  for ma in maps:
    for map in ma:
      # print(map)
      D,S,R = map.split(' ')
      # print(f"D={D} S={S} R={R}")
      source = range(int(S),(int(S)+int(R))) 
      if s in source:
        # print(f"s={s} in {source}")
        offset = s - int(S)
        destination = range(int(D),(int(D)+int(R)))
        s = (int(D) + offset)
        # if s < lowest:
        #   lowest = s
        break
  if s < lowest:
    lowest = s      
print(f"lowest: {lowest}")   
#the destination range start, the source range start, and the range length.