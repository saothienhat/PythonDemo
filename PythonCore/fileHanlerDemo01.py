
filePath = "C:\\testpython.txt"

##### FILE OBJECT Attributes

# Syntax
# file_object = open(filename [,mode] [, isBuffering])

# file opening example in Python
try:   
   fileOpener = open(filePath, "wb")
   print("Result of reading file........")
   print ("\tFile Name: ", fileOpener.name)
   print ("\tMode of Opening: ", fileOpener.mode)
   print ("\tIs Closed: ", fileOpener.closed)
   #print ("\tSoftspace flag : ", fo.softspace)

   
finally:
   # Close opened file
   fileOpener.close()



##### FILE Reading

# read the entire file as one string
# with open(filePath) as f:
f = open(filePath, 'r')
data = f.read()
print("data: ", data)

# Iterate over the lines of the File
#with open(filePath) as f:
for line in f :
    print("Line: ", line)
#    print(line, end=' ')
# process the lines


##### FILE Writing

with open(filePath , 'wt') as f:
    f.write ('hi there, this is a first line of file.\n')
    f.write ('and another line.\n')