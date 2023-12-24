import sys
import os
from pathlib import Path
import re

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Data.txt")).read().strip()
L = D.split("\n")
os.system("cls")

print(L)