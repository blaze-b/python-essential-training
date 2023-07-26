import sys

f = open("09_io_file/wasteland.txt", mode='at',
         encoding=sys.getdefaultencoding())

f.writelines([
    'Son of man,\n',
    'You cannot say, or guess, ',
    'for you know only,\n',
    'A heap of broken images, ',
    'where the sun beats\n'
])

f.close()
