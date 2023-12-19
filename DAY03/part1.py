import sys
import os
from pathlib import Path
import re

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Example.txt")).read().strip()
L = D.split("\n")

gears = ()
ii = 0
for l in L:
  i = str(l).find('*')
  print(l)
  if i > -1:
    # gear found
    r=re.findall(r"\d{1,}",l)
    print(r)
    if ii > 0:
      # not first line  
      r=re.findall(r"\d{1,}",L[ii-1])
      print(r)
    if ii < len(L)-1:
      # not last line
      r=re.findall(r"\d{1,}",L[ii+1])
      print(r)
  ii+=1