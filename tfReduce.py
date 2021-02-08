import sys
import re

currWord = None
currCount = 0
word = None

for line in sys.stdin:
     line = line.strip()
     word, count = line.split('\t', 1)
     try:
          count = int(count)
     except ValueError:
          continue

     if currWord == word:
          currCount += count
     else:
          if currWord:
               print('%s\t%s' % (currWord, currCount))
          currCount = count
          currWord = word

if currWord == word:
     print('%s\t%s' % (currWord, currCount))