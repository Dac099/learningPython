fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From ') and not line.startswith('From:'):
        auxLine = line.split()
        print(auxLine[1])

numList = list()

while True:
    num = input('Enter the number or write done to finish: ')
    if num == 'done': break
    numList.append(float(num))
print('Max value is: ', max(numList))
print('Min value is: ', min(numList))