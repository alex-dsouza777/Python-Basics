#Open function reads the file contents and Close function closes the files.
#f = open('sample.txt', 'r') #Opens file in current directory
f = open('sample.txt') #By default mode is r
#data = f.read() #read function will read the file
data = f.read(2) #Will read first 2 characters of the file
print(data)
f.close()