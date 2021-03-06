import gzip

import re

import os
DIR = "9902"
for filename in os.listdir(os.getcwd() +"/" + DIR):
    if filename[:4] != "math" or filename[-3:] != ".gz":
        continue
    with gzip.open(DIR + "/" + filename) as ar:

        for line in ar:
            try:
                x = re.search("([0-9]+\.)[0-9]{9,}", line.decode("utf-8"))
                if x:
                    print(filename)
                    print(line)
                    print(x.group(0))
            except UnicodeDecodeError:
                pass
