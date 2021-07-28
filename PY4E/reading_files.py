fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count+=1
print(count)

#If the file es relatively small compared to the size of your memory, you can rea the whole file into one string with the method read()
inp = fhand.read()
print(len(inp))
print(inp[:20])

#Asking for the file name

while True:
    fname = input('> ')
    try:
        fhand = open(fname)
        break
    except:
        print(f'File cannot be opened: {fname}')
        continue

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count += 1

print(count)