# Opening files -------------------------------------------------------------------

fhand = open('mbox-short.txt') #We get the handle to manipulate the file
count = 0
for line in fhand:
    count = count + 1
    line = line.rstrip() #With this line remove the double spacing of our program
    if line.startswith('From:'):#Searching data from the file
        print(line)

print('Line count: ', count) #132045 lines


#Another way to structure our programs is: -----------------------------------------

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #If the method find return < -1 > it means that the line cannot be found
    #So if the line.find() == -1 we scape this loope instead we print the line
    if line.find('@uct.ac.za') == -1: continue
    print(line)

#Using try and except --------------------------------------------------------------

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were ',count,' subject lines in ', fname)        


#Writing files ---------------------------------------------------------------------

fout = open('output.txt', 'w')
print(fout)
fout.close()
