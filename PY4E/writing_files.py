#To write a file, you have to open it with mode “w” as a second parameter:
fout = open('output.txt','w')

#If the file already exists, opening it in write mode clears out the old data and starts
# fresh, so be careful! If the file doesn’t exist, a new one is created.

fout.write('This is test that prints lines in a new file\n')
fout.write('This must be the second line in the file\n')

fout.close()