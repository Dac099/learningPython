str = 'X-DSPAM-Confidence:0.8475'
stringToNumber = str.find(':')
stringToNumber = float(str[stringToNumber + 1:])
print(stringToNumber)
print(type(stringToNumber))