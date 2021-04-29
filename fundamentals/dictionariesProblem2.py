import string
# $!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~   string.puntuation
fname = input('File name: ')

while True:
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened ", fname)

