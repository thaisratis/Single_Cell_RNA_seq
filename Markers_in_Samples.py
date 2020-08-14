# coding=utf-8
from sys import argv
import os

WT = argv[1] # A file in which each columns is one different cell type, and the lines are the gene's id
 ''' File example:
Cell1	Cell2	Cell3	Cell4	Cell5	Cell6	Cell7	Cell8	Cell9	Cell10	Cell11
Acta1	Adh1	Adam33	Adam8	Bach2	Adam19	Kcna1	Adamts14	Bcl2	Abcc9	Cdh15
Actc1	Adh7	Adamts10	Adgre4	Bank1	Anxa1	Plp1	Cd244	Birc5	Angpt1	Egfr
Actn2	Amigo2	Adamts5	Adgre5	Bcl11a	Ap1s3		Cd27	Cd160	Angpt2	Fgfr4
Adipor1	Aph1b	Akr1c18	Ahr	Birc3	Ass1		Chsy1	Cd163l1	Anpep	Flnc
 '''
itemList = os.listdir("Path") # A path with expression matrix files
outputfile = open('Path/Results_Markers.txt' , 'a')
genes=[]

result = [0] *11 # Ceate a list with the number of cell's markers (e.g. in my case, I had 11 cell types)
boolean = False

# For each file into the folder
for item in itemList:

	ifile = open('Path' + str(item), 'r')

	header = ifile.readline()
	boolean = False
	result = [0] *11
	genes=[]

	# For line into the file
	for line in ifile:
		
		line2 = line.split('\t')
		gene_symbol = line2[0] # Take the name of the gene to search into the marker's file


		WT_Genes = open(WT, 'r') # Marker's file
		WT_Genes.readline()

		for i in WT_Genes:

			linha = i.split('\t')
			linha[len(linha)-1] = linha[len(linha)-1][:-1]

			# Count the number of gene's markers by each type that are found in the expression files
			for x in range(0,len(linha)):
				if(gene_symbol==linha[x]):
					
					result[x]+=1
					break

		WT_Genes.close()

	outputfile.write(str(item) + "\n" + 
		"B-cells\t" + str(result[4])	+ "\n"+
		"Cardiomyocytes\t" + str(result[0])+ "\n" +
		"Dendritic\t"	+ str(result[5])+ "\n"+
		"Endothelial\t" + str(result[1])+ "\n"	+
		"Fibroblasts and Myofibroblasts\t" + str(result[2])+ "\n"+
		"Glial cells\t" + str(result[6])+ "\n"	+
		"Macrophages and Monocytes\t"	+ str(result[3])+ "\n"+
		"Mural cells, Vascular smooth muscle cells and Pericytes\t" + str(result[9]) + "\n"+
		"Myoblasts\t" + str(result[10]) + "\n"+		
		"Natural Killer Cells\t" + str(result[7])+ "\n" +
		"T-cells\t"	+ str(result[8]) + "\n\n") 
		
	
	ifile.close()
outputfile.close()
