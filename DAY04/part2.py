import os

file = os.path.dirname(__file__)

D = open(os.path.join(file,"Data.txt")).read().strip()
C = D.split('\n')
play = []
play2 = []
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
  points = 0
  wins=0
  
  for num in nums:
    if num in winnings:
      wins +=1
      if points == 0:
        points += 1
      else:
        points = points * 2
  play.append((Cards[0],winnings,nums,points,wins))
  totalpoints += points

def duplicate(i): 
  nb = play[i][4]
  if nb > 0:
    # print(f'Card {play[i][0]} : i={i} - nb = {nb}')
    j = i + 1
    while (j < ((i+1) + nb)):
      # print(f'j={j}')
      play2.append(play[j])
      duplicate(j)       
      j+=1
  

ii = 0
while ii < len(play)-1:
  duplicate(ii)
  ii+=1

print(len(play)+len(play2))
