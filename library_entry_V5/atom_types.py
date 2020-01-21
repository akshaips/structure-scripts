import os
import sys

topology = sys.argv[1]
open_top = open(topology,"r")
read_top = open_top.readlines()
open_top.close()
ligand_file = sys.argv[2]
ligand_file_open = open(ligand_file,"r").readlines()
ligand_name = sys.argv[3]
ligand_list = []
top_list = []
def ligand_file():
	n = 0
	while n < len(ligand_file_open):
		ligand_file_split = ligand_file_open[n].split()
		if (ligand_file_split[0] == "ATOM" or ligand_file_split[0] == "HETATM"):
			if ligand_file_split[3] == ligand_name:
				ligand_list.append(ligand_file_split[2])
		n += 1
	atoms_list()
	
def atoms_list():
	n = 0
	initial_n = 0
	n_list = []
	atom_lists = []
	while n < len(read_top):
		top_split = read_top[n].split()
		if len(top_split) > 1:
			if top_split[0][0] != ";":
				if top_split[0] == "[" and top_split[1] == "atoms" and top_split[2] == "]":
					initial_n = n
				if n > initial_n  and initial_n != 0 and top_split[0] == "[" and top_split[2] == "]":
					break
				if initial_n != 0 and n > initial_n:
					top_list.append(top_split[4])
					top_list.append(top_split[1])
					top_list.append(top_split[5])
		n += 1	
	output()

def output():
	writing = open("ATOM_TYPES.txt","w")
	entry = ""
	n = 0
	while n < len(top_list):
		if n % 3 == 0:
			entry += (top_list[n] + "\t" + top_list[n] + "\t" + top_list[n+1] + "\t" + top_list[n+2] + "\n")
		n += 3
	writing.write(entry)
		
ligand_file()
