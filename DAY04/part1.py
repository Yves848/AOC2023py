import os

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Data.txt")).read().strip()
C = D.split('\n')
play = {}
totalpoints = 0
for l in C:
  Cards = l.split(":")
  numbers = Cards[1].split('|')
  winnings = []
  for c in (numbers[0].strip().split(' ')):
    if str(c).strip() != '':
      winnings.append(c)
  nums =  []
  for c in (numbers[1].strip().split(' ')):
    if str(c).strip() != '':
      nums.append(c)
  play[Cards[0]]=(winnings,nums)
  points = 0
  for num in nums:
    if num in winnings:
      if points == 0:
        points += 1
      else:
        points = points * 2

  totalpoints += points
print(play)
print(totalpoints)