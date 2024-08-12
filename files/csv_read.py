fileConnection =  open("example.txt", "r")   #normal way to read a file
lines  = fileConnection.readlines()  # 
for lin in lines[:6]:  # read till line 6 
   print(lin.strip())    # using loop print it and ignore thw widespaces

header = lines[0]
field_names = header.strip().split(',')
print (field_names)
for row in lines[1:]: 
  vals = row.strip().split(',')
  if vals[5] != "NA":
    print("{}:{};{}".format(
      vals[0],
      vals[4],
      vals[5] ))