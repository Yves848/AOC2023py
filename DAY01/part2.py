import re
with open('Data.txt',encoding="utf-8") as f:
  file = f.read().split('\n')
f.close

w = ("one","two","three","four","five","six","seven","eight","nine")
w2 = ("o1e","t2o","th3ee","f4ur","f5ve","s6x","se7en","ei8ht","n9ne")

total = 0
for l in file:
  print(l)
  for i in range(len(w)):
    l = l.replace(w[i],w2[i])

  print(l)
  nums = re.findall(r"\d{1}",l)
  val = (int(nums[0])*10) + int(nums[-1])
  print(nums)
  print(val)
  total += val

print(total)