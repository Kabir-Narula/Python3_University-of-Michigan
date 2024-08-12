file_obj = open("example.txt","w")
for number in range(13):
  square = number * number
  file_obj.write(str(square))
file_obj.close()