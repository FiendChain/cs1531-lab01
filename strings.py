strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for word in strings:
    sentence += (word + " ")
print(sentence.rstrip())
