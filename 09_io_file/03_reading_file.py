import sys

f = open("09_io_file/wasteland.txt", mode='rt',
         encoding=sys.getdefaultencoding())

print(f)

print(f.read(32))
print(f.read())
print(f.seek(0))

print(f.readline())
print(f.readline())
print(f.readline())
print(f.seek(0))


print(f.readlines())

f.close()
