import sys

f = open("09_io_file/wasteland.txt", mode='wt',
         encoding=sys.getdefaultencoding())

print(f)

# help(f)

f.write('What are the roots that clutch, ')

f.write('What branches grow\n')

f.write('Out of this stony rubbish? ')

f.close()
