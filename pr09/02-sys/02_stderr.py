import sys

fsock = open('error.log', 'w')
sys.stderr = fsock
raise TypeError('this error will be logged')
