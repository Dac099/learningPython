fname = input('Enter the file name: ')

while True: 
    try:
        fhand = open(fname)
        break
    except:
        print('File cannot be found', fname)
        continue

count = 0
for line in fhand: 
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        strToNumber = line.find(':')
        strToNumber = float(line[strToNumber + 1:])
        count += strToNumber
print('Average spam confidence: ', count)    
