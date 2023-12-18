import re

with open('Data.txt',encoding="utf-8") as f:
  file = f.read().split('\n')
f.close
total = 0
for l in file:
  print(l)
  nums = re.findall(r"\d{1}",l)
  val = (int(nums[0])*10) + int(nums[-1])
  print(nums)
  print(val)
  total += val

print(total)