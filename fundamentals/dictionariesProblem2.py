import string
# $!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~   string.puntuation
fname = input('File name: ')

while True:
    try:
        fhand = open(fname)
        break
    except:
        print("File cannot be opened ", fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    #maketrans() create a table. The first argument will be map to the second argument and the third argument will be map with none.
    #translate() will be replaced the key value of a table <<dictionarie>> with his value.
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


