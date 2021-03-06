import gzip
import tarfile
import re
import os

DIR = "2102"
# functon to actually read a tex file
def reader(filename, ar):
    printed = False
    for line in ar:
        try:
            x = re.search("([0-9]+\.)[0-9]{9,}", line.decode("utf-8"))
            if x:
                if not printed:
                    print(filename)
                    printed = True
                print("    " + line.decode("utf-8").strip())
                print("    " + x.group(0))
        except UnicodeDecodeError:
            pass
for filename in os.listdir(os.getcwd() +"/" + DIR):
    # math only appears as an identifier post March 2007 
    #if filename[:4] != "math" or filename[-3:] != ".gz":
    if filename[-3:] != ".gz":
        continue
    if tarfile.is_tarfile(DIR + "/" + filename):
        with tarfile.open(DIR + "/" + filename, "r:gz") as ar:
            for member in ar.getmembers():
                if member.name[-4:] != ".tex":
                    continue
                f = ar.extractfile(member)
                reader(filename, f)
    else:
        with gzip.open(DIR + "/" + filename) as ar:
            reader(filename, ar)
