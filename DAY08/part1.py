import os


file = os.path.dirname(__file__)

directions, *rest = open(os.path.join(file,"Example.txt")).read().split('\n\n')
plans = list(map(lambda plan: plan.replace('(','').replace(')',''),rest[0].split('\n')))
network = {}
for plan in plans:
  key,*pair = plan.split("=")
  pair1,pair2 = pair[0].split(',')
  network[key]=tuple((pair1,pair2))

print(directions)
print(network)