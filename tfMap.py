import sys
import re
import os
for line in sys.stdin:
     line  = line.strip()

     tokens = filter(None, re.split('[\W+_]', line))
     # fDir = os.environ['mapreduce_map_input_file']
     for token in tokens:
          word = re.sub('[^a-zA-Z0-9]+', '', token.lower())
          print('%s\t%s' % (word, 1))