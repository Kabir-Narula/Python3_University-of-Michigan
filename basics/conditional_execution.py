# x= 15

# if x %2 == 0:
#   print(x, "is even")
# else: 
#   print(x, "is odd")
  
x = 15

if x % 3 == 0:
    if x % 5 == 0:
        print(x, "is divisible by both 3 and 5")
    else:
        print(x, "is divisible by 3 but not by 5")
else:
    if x % 5 == 0:
        print(x, "is divisible by 5 but not by 3")
    else:
        print(x, "is not divisible by either 3 or 5")
