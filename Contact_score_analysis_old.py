import os
import glob 
import time

files = glob.glob("*.txt")

list_aa = ['ala ','ARG ','ALA ','arg ','ARG ','asn ',	'ASN ','asp ',	'ASP ','glu ',	'GLU ','gln ',	'GLN ','his ',	'HIS ','leu ',	'LEU ','met ',	'MET ','phe ',	'PHE ','pro ',	'PRO ','ser ',	'SER ','thr ',	'THR ','trp ',	'TRP ','tyr ',	'TYR ','val ',	'VAL ', 'LYS ', 'lys ', 'CYS ', 'cys ', 'ILE ','ile ']

list_1 = []

for file in files:
	file_open = open(file,"r")
	file_read = file_open.read()
	n = 0
	while n+1 < len(file_read):
		residue_file = file_read[n-2] + file_read[n-1] + file_read[n] + file_read[n+1]
		if residue_file in list_aa:
			if file_read[n+4] != " " and file_read[n+3]!= " ":
				list_1.append(file_read[n-2] + file_read[n-1] + file_read[n]+ file_read[n+1] + file_read[n+2] + file_read[n+3] + file_read[n+4])
			elif file_read[n+4] == " ":
				list_1.append(file_read[n-2] + file_read[n-1] + file_read[n]+ file_read[n+1] + file_read[n+2] + file_read[n+3])
			elif file_read[n+3] == " ":
				list_1.append(file_read[n-2] + file_read[n-1] + file_read[n]+ file_read[n+1] + file_read[n+2])
		n += 1

list_2 = []
for elements in list_1:
	if elements not in list_2:
		list_2.append(elements)

print (list_2)

for elements in list_2:
	os.system('grep "' + elements + '" ' + " * > " + elements[:3] + "_" + elements[4:] + ".out")
	
		
files = glob.glob("*.out")

combined_file = open("combined_file.txt","w")

for file in files:
	open_file = open(file,"r")
	read_file = open_file.read()
	split_file = read_file.split('\n')
	write_file = open(file,"a")
	list_1 = []
	for lines in split_file:
		if lines != "":
			inverse = 1 / float(lines[-5:])
			list_1.append(inverse)
	
	sum = 0
	for elements in list_1:
		sum = sum + elements
	write_file.write(str(sum))
	
	combined_file.write(file[:-4]+ " = " + str(sum) + "\n")


	
