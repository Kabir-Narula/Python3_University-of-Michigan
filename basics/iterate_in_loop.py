nums = [1,2,3,4,5,6,7,8,9,10]
accum = 0
for w in nums:
  accum += w
print(accum) # happens outside the for loop


for w in nums:
  accum += w
  print(accum) # happens inside the for loop


for w in range(12):
  accum += w
print(accum) # 