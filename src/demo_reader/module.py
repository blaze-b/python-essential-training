import sys
import urllib

# import urllib.request

from urllib import request

print(type(urllib))

print(type(request))

print(urllib.__path__)

print(request.__all__)

# print(sys.path)

print(sys.path[0], sys.path[1], sys.path[-5:])
