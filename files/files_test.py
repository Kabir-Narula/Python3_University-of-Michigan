# reading a file
fileRef = open("example.txt", "r")#r means reading a file, open example.txt for reading
contents = fileRef.read()
print(contents[:100])
fileRef.close()


# reading a file
# fileRef = open("example.txt", "r")
# lines = fileRef.readlines()
# for lin in lines[:4]:
      #print(lin.strip())  # strip gets rid of wideSpaces and lines
# fileRef.close()
