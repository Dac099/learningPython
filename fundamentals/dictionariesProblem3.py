fname = input('Enter the file name: ')

while True:
    try:
        fhand = open(fname)
        break
    except:
        print('File cannot be found ',fname)

daysOfTheWeek = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        daysOfTheWeek[words[2]] = daysOfTheWeek.get(words[2], 0) + 1
print(daysOfTheWeek)