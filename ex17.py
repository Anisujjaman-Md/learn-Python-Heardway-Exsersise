from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying file from %s to %s " %(from_file, to_file))

#we coould do these two on one line too. how?

in_file = open(from_file)
indata = in_file.read()

print ("The input file is %d byte long." %len(indata))
print("Does the output file exist? %r" %exists(to_file))
print("Ready, hit Enter to continue. CTRL -C to abourt.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close
