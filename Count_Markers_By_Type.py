# coding=utf-8
from sys import argv
import os

WT = argv[1] # A file with a transcript's list

itemList =  os.listdir("Path") # A path with marker's file (i.e. a folder with separately files from the markers by each type of cells)
''' For example:
File1 has:
Marker1
Marker2
Marker3

File2 has:
Marker1
Marker2
Marker3

File3 has:
Marker1
Marker2
Marker3

And each file has markers from different cell types
'''

outputfile = open('Path/outputfile.txt' , 'w')
genes=[]

result = 0
boolean = False

# For each file into the folder
for item in itemList:

	ifile = open('Path' + str(item), 'r') 

	boolean = False
	result = 0
	genes=[]

	for line in ifile:

		# Open the file with the transcript's list
		WT_Genes = open(WT, 'r')
		WT_Genes.readline()

		# Check which transcripts are markers and its type
		for i in WT_Genes:

			if(line==i):
				result+=1

		WT_Genes.close()

	# Write the name of cell type and how many transcripts were found in the markers list of this cell
	outputfile.write(str(item) + "\t" + str(result)	+ "\n") 
	
	ifile.close()
outputfile.close()