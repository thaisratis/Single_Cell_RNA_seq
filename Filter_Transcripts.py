from sys import argv
import os


# List all the folder with all expression matrix files
itemList =  os.listdir("Path")

# For each file into the folder
for item in itemList:

	# Open the file and create the output file
	input_file = open("Path" + str(item), "r")
	output = open("Path/Filtered_" + str(item), "w") 

	#Read the header and write it on the output file
	header = input_file.readline()
	output.writelines(header)

	# Create the first filter which is expression in at least 5% of the cells
	head = header.split("\t")
	length = (len(head) -1) # Take the number of cells (i.e., the number of columns -1 (the column with transcript name))
	cells_percent = ((length * 5) / 100)

	cells_counts = 0

	# Read the lines from each file
	for line in input_file:
		linha = line.strip().split("\t")
		expression = linha[1:] # Take off the first column, because it's the transcript ID
		ids = linha[0]
		gene_expression = list(map(float, expression)) # Create a new list with all expression values converted into float
		
		#Count how many fpkm expression values are greather than 0.001
		for i in gene_expression:

			if(i > 0.001):
				cells_counts = cells_counts + 1
			else:
				continue;

		# Check if the number of cells that have expression value greather than 0.001 is bigger than 5% of the cells
		# If the transcript have expressiion value greather than 0.001 in at least 5% of the cells, we take it
		if (cells_counts >= cells_percent):
			output.writelines(line)
			cells_counts = 0
		else:
			cells_counts = 0

	output.close()
	input_file.close()