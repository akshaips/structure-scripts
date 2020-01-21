import os
import sys

print ("\n\n\nBelow entries in aminoacids.rtp entry\n\n\n")

filename = sys.argv[1]
open_top = open(filename,"r")
open_top1 = open(filename,"r")
read_top = open_top.read()
top_lines = open_top1.readlines()
atom_type_read = open("ATOM_TYPES.txt","r").read()
atom_type = atom_type_read.split()
open_top.close()
open_top1.close()
top_split = read_top.split()
res = sys.argv[2]

def atoms_list():
	n = 0
	initial_n = ""
	n_list = []
	atom_lists = []
	check = 0
	while n < len(top_split):
		if top_split[n] == "[" and top_split[n+1] == "atoms" and top_split[n+2] == "]":
			check = 1
		if check == 1 and top_split[n] == res and top_split[n-3] == "1":
			initial_n = n
		if initial_n != "" and n+initial_n <len(top_split) and top_split[n+initial_n] == "[":# and top_split[initial_n+n+2] == "]":
			n_list.append(n+initial_n)
			break
		n += 1	

	n = initial_n 
	while n < n_list[0]:
		atom_lists.append(top_split[n])
		n += 1

	printing_atoms(atom_lists)

def printing_atoms(atom_lists):
	m = 0
	print ("[ " + res + " ]")
	print (" [ atoms ] ")
	while m < len(atom_lists):
		if atom_lists[m] == res:
			n = 0
			renamed_atom = ""
			while n < len(atom_type):
				if atom_lists[m+1] == atom_type[n]:
					renamed_atom = atom_type[n+1]
					break
				n += 1
			print (renamed_atom+"\t"+atom_lists[m-2]+"\t"+atom_lists[m+3]+"\t"+atom_lists[m+2])
		m += 1
	


def bonds_list():
	n = 0
	initial_n = 0
	final_n = 0
	substract = 0
	n_list = []
	bond_lists = []
	while n < len(top_lines):
		top_split_1 = top_lines[n].split()
		if len(top_split_1) > 1:
			if top_split_1[0][0] != ";":
				if top_split_1[0] == "[" and top_split_1[1] == "bonds" and top_split_1[2] == "]":
					initial_n = n
			if len(top_lines)-1  == n:
				final_n = n
				break
			if len(top_split_1) > 0:
				if initial_n != 0 and n > initial_n and top_split_1[0] == "[":
					final_n = n
					break
			if len(top_split_1) <= 2:
				substract += 1
		n += 1

	m = initial_n + 1
	while m < int(final_n) - substract:
		if top_lines[m][0] != ";" or not top_lines[n].rstrip():
			bond_lists.append(top_lines[m])
		m += 1

	printing_bonds(bond_lists)

def printing_bonds(bond_lists):
	m = 0
	print ("\n")
	print (" [ bonds ]")
	while m < len(bond_lists):
		n = 0
		while n < len(atom_type):
			bond_list_split = bond_lists[m].split()
			if bond_list_split[0] == atom_type[n]:
				renamed_bondatom1 = atom_type[n-2]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			bond_list_split = bond_lists[m].split()
			if bond_list_split[1] == atom_type[n]:
				renamed_bondatom2 = atom_type[n-2]
				break
			n += 1
		print (renamed_bondatom1 + "\t" + renamed_bondatom2)
		m += 1	

atoms_list()
bonds_list()
