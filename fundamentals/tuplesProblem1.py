
while True:
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
        break
    except:
        print("File cannot be found: ", fname)
        continue


emails = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        email = words[1].split('@')
        emails[email[1]] = emails.get(email[1], 0) + 1

emailCount = list()
for count, email in list(emails.items()):
    emailCount.append((count,email))

emailCount.sort(reverse=True)
print(emailCount[0])