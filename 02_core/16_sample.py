from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')

story_words = []

# for line in story:
#     line_words = line.split()
#     for word in line_words:
#         story_words.append(word)
# print(story_words)

# For unicode check as it is http data
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()

print(story_words)
