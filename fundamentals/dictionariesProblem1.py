fhand = open('words.txt')
ourWords = dict()

# for line in fhand:
#     line = line.rstrip()
#     auxLine = line.split()
#     for word in auxLine:
#         if word in ourWords:
#             ourWords[word] += 1
#         else:
#             ourWords[word] = 1
            
# print(ourWords)


#The method <GET> in dictionaries return the value of parameter that we passed instead return the value of the key

for line in fhand:
    line = line.rstrip()
    auxLine = line.split()
    for word in auxLine:
        #If get don't foud word in the dictionarie will return 0 + 1, instead will return the value of the key + 1
        ourWords[word] = ourWords.get(word, 0) + 1
            
print(ourWords)            

 