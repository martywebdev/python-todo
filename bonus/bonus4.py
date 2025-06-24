filenames = ['1.Raw Data.txt', '2.Reposts.txt', '3.Presentations.txt']


for filename in filenames:
    filename = filename.replace('.', '-') # creating new string because strings are immutable
    print(filename)