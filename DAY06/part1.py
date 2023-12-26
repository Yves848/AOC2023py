lines = open(0).read().split('\n')

times = list(map(int,["".join(lines[0].split(':')[1].split())]))
records = list(map(int,["".join(lines[1].split(':')[1].split())]))

n=1

for time, distance in zip(times,records):
  margin = 0
  for hold in range(time):
    if hold * (time - hold) > distance:
      margin +=1
  n *= margin

print(n)