import sys
import os
from pathlib import Path
import re

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Data.txt")).read().strip()
L = D.split("\n")
os.system("cls")

gears = []
ii = 0
sum = 0
for l in L:
  i = 0
  print(f"{ii} - {l}")
  while i > -1:
    i = str(l).find('*',i+1) 
    if i > -1:
      # Same line
      gear = []
      # print(f'Index : {i}')
      num = ""
      j = i-1
      while (j > 0 and  l[j].isdigit()):
        num = l[j] + num
        j-= 1
      if (num.isnumeric()):
        gear.append(num)
      num = ""
      j = i+1
      while (j < len(l) and l[j].isdigit()):
        num = num + l[j]
        j+= 1
      if (num.isnumeric()):
        gear.append(num)

      if ii > 0:
        # Line UP  
        l2 = L[ii-1] 
        finds=re.findall(r"\d{1,}",l2)
        i1 = 0
        for f in finds:
          lf = len(f)
          i1 = str(l2).index(f,i1) 
          if (i in range(i1-1,i1+lf+1)):
            gear.append(f)
          i1 = i1 + lf
        # print(finds)
              
      if ii < len(L)-1:
        # Line Down
        l2 = L[ii+1] 
        finds=re.findall(r"\d{1,}",l2)
        i1 = 0
        for f in finds:
          lf = len(f)
          i1 = str(l2).index(f,i1) 
          if (i in range(i1-1,i1+lf+1)):
            gear.append(f)
          i1 += lf
        # print(finds)
      print(gear)

      if (len(gear) >= 2):
        gears.append(int(gear[0])*int(gear[1]))
  ii+=1

# print(gears)
sum = 0
for gear in gears:
  sum += int(gear)
print(sum)