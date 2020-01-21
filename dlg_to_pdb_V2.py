import os
import sys

runs = []
	
if len(sys.argv) < 2:
	print("USAGE:\n")
	print("   python dlg_to_pdb.py filename.dlg")
	print("\n   eg: python dlg_to_pdb.py dock.dlg")
	print("\nGive inputs : \n\n   'All' for all to be extracted separated\
		\n	'0' to extract everything in one file \n\
	'2' to extract only second structure")
	exit()
else:
	dlg_file = sys.argv[1]
	cluster_extraction = input("Cluster extract (y/n):")
	if cluster_extraction == "n" or cluster_extraction == "N":
		model_number = input('Model number ("All"/0(to write in one pdb)/\'model number to be extracted\'(eg:1,2,3)) :   ')
	elif cluster_extraction == "y" or cluster_extraction == "Y":
		print ("Enter cluster number")
	else:
		print ("Enter valid input")
		exit()
	os.system("mkdir " + dlg_file[:-4])
	
def cluster_extract(cluster_number):
	file_open = open(dlg_file, "r").readlines()
	
	conformations = []
	for entry in file_open:
		if "RANKING" in entry:
			entry_split = entry.split()
			if int(entry_split[0]) == cluster_number:
				conformations.append(str(entry_split[2]))
			else:
				None
	
	return (conformations)
	
	
def Read_file(runs,model_number):
	file_open = open(dlg_file, "r").readlines()
	count = 0
	n = 0
	conformation_number = []
	while n < len(file_open):
		file_split = file_open[n].split()
		if len(file_split) >= 1 \
				and (file_split[0] == "DOCKED:" and file_split[1] == "ATOM"):
			runs.append(file_open[n])
		if len(file_split) >= 1 and file_split[0] == "Run:":
			count += 1
			conformation_number.append(str(count))
		n += 1
	
	
	if cluster_extraction == "n" or cluster_extraction == "N":
		Split_to_pdb(runs, count,dlg_file[:-4],model_number)
		print(count)
	elif cluster_extraction == "y" or cluster_extraction == "Y":
		conformations = cluster_extract(cluster_number)
		for model_number in conformations:
			Split_to_pdb(runs, count,dlg_file[:-4] + "/" + "Cluster_" + str(cluster_number),model_number)
		print(str(len(conformations)) + "/" + str(count) + " conformations")


def Split_to_pdb(runs, count,folder_name,model_number):
	total_atoms = 0
	n = 0
	total_atoms = len(runs)
	if model_number == "0":
		writing = open(folder_name + "/all_models.pdb", "w")
		models = ""
		mdl_number = 1
		m = 0
		while m < len(runs):
			models += ("MODEL	" + str(mdl_number) + "\n")
			n = 0
			while n < int(total_atoms/count):
				models += (runs[m+n][8:])
				n += 1
			mdl_number += 1
			models += ("ENDMDL\n")
			m += int(total_atoms/count)
		writing.write(models)
	elif model_number == "All" or model_number == "ALL"\
			or model_number == "all":
		mdl_number = 1
		m = 0
		while m < len(runs):
			writing = open(folder_name + "/" + str(mdl_number) +
						   "_" + str(count) + ".pdb", "w")
			models = ""
			models += ("MODEL	" + str(mdl_number) + "\n")
			n = 0
			while n < int(total_atoms/count):
				models += (runs[m+n][8:])
				n += 1
			mdl_number += 1
			models += ("ENDMDL\n")
			writing.write(models)
			writing.close()
			m += int(total_atoms/count)
	else:
		mdl_number = 1
		m = int((int(model_number) * (total_atoms/count)) -
				(total_atoms/count))
		while m < int(model_number) * (total_atoms/count):
			writing = open(folder_name + "/" + str(model_number) +
						   "_" + str(count) + ".pdb", "w")
			models = ""
			models += ("MODEL	" + str(model_number) + "\n")
			n = 0
			while n < int(total_atoms/count):
				models += (runs[m+n][8:])
				n += 1
			mdl_number += 1
			models += ("ENDMDL\n")
			writing.write(models)
			writing.close()
			m += int(total_atoms/count)


		
if cluster_extraction == "n" or cluster_extraction == "N":
	Read_file(runs,model_number)
elif cluster_extraction == "y" or cluster_extraction == "Y":
	cluster_number = int(input("Cluster number :"))
	os.system("mkdir " + dlg_file[:-4] + "/Cluster_" + str(cluster_number))
	Read_file(runs,"0")

