
while True:
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
        break
    except:
        print("File cannot be found: ", fname)
        continue

messages = dict()
emails = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        email = words[1].split('@')
        emails[email[1]] = emails.get(email[1], 0) + 1
        messages[words[1]] = messages.get(words[1], 0) + 1
print(emails)
print(messages)


#Maximum loop
largest = None
idx = str()
for key in messages:
    if largest is None or messages[key] > largest:
        largest = messages[key]
        idx = key
print(idx, messages[idx])
