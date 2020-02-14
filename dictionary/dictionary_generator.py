import csv
import os
import pathlib
from shutil import copyfile
from shutil import move
from shutil import rmtree

with open('glossary.csv', 'r') as glossary:
    csvreader = csv.reader(glossary)
    data = [line for line in csvreader]
    rows = csvreader.line_num

data.sort(key=lambda x: x[0].lower())
    
dictionary = open(".aspell.it.pws","w")
dictionary.write ("personal_ws-1.1 it "+str(rows)+'\n')
for line in data:
    dictionary.write (line[0].replace(" ","G\n").replace(")","").replace("(","") + "G\n")

file = pathlib.Path("custom_dictionary")
if file.exists():
	dictionary.flush()
	os.mkdir("./temp/")
	copyfile("./.aspell.it.pws", "./temp/.aspell.it.pws")
	move('./.aspell.it.pws', './.aspell.it.pws.old')
	with open("./temp/.aspell.it.pws", "a") as myfile:
		with open("custom_dictionary") as f:
			s = f.read()
			myfile.write(s)
	move('./temp/.aspell.it.pws', './.aspell.it.pws')
	rmtree('./temp/')