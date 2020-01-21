import os
import sys

print ("\n\n\nEnter below ones in ffbonded.itp\n\n\n")

filename = sys.argv[1]
open_top = open(filename,"r")
top_lines = open_top.readlines()
atom_type_read = open("ATOM_TYPES.txt","r").read()
atom_type = atom_type_read.split()
open_top.close()
res = sys.argv[2]
list_angle = []
list_bond = []

def make_list(list_of):
	n = 0
	initial_n = 0
	final_n = 0
	substract = 0
	new_list = []
	while n < len(top_lines):
		top_split = top_lines[n].split()
		if len(top_split) > 1:
			if top_split[0][0] != ";":
				if top_split[0] == "[" and top_split[1] == list_of and top_split[2] == "]" and list_of != "impropers" and initial_n == 0:
					initial_n = n
			if len(top_lines)-1  == n:
				final_n = n
				break
			if len(top_split) > 0:
				if initial_n != 0 and n > initial_n and top_split[0] == "[":
					final_n = n
					break
			if len(top_split) <= 2:
				substract += 1
			
		n += 1

	if list_of == "impropers":
		new_list = []
		n = 0
		initial_n = 0
		final_n = 0
		substract = 0
		while n < len(top_lines):
			top_split = top_lines[n].split()
			if len(top_split) > 3:
				if top_split[0][0] != ";":
					if top_split[0] == "[" and top_split[1] == "dihedrals" and top_split[2] == "]" and top_split[4] == "impropers":
						initial_n = n
			if len(top_lines)-1  == n:
				final_n = n
				break
			if len(top_split) > 0:
				if initial_n != 0 and n > initial_n and top_split[0] == "[":
					final_n = n
					break
			n += 1
		
	m = initial_n + 1
	while m < int(final_n) - substract:
		if top_lines[m][0] != ";" or not top_lines[n].rstrip():
			new_list.append(top_lines[m])
		m += 1
		
	if list_of == "bonds":
		printing_bonds(new_list)
	elif list_of == "dihedrals":
		printing_dihes(new_list)
	elif list_of == "angles":
		printing_angles(new_list)
	elif list_of == "impropers":
		if len(new_list) > 100:
			printing_impropers(new_list)
	

def printing_impropers(improper_list):
	m = 0
	multiple_imp_dihedrals_list = []
	improper_rtp = ""
	while m < len(improper_list):
		n = 0
		while n < len(atom_type):
			imp_list_split = improper_list[m].split()
			if imp_list_split[0] == atom_type[n]:
				renamed_diheatom1 = atom_type[n-1]
				atom1 = atom_type[n-2]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			imp_list_split = improper_list[m].split()
			if imp_list_split[1] == atom_type[n]:
				renamed_diheatom2 = atom_type[n-1]
				atom2 = atom_type[n-2]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			imp_list_split = improper_list[m].split()
			if imp_list_split[2] == atom_type[n]:
				renamed_diheatom3 = atom_type[n-1]
				atom3 = atom_type[n-2]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			imp_list_split = improper_list[m].split()
			if imp_list_split[3] == atom_type[n]:
				renamed_diheatom4 = atom_type[n-1]
				atom4 = atom_type[n-2]
				break
			n += 1
		if (renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+imp_list_split[4]+"\t"+imp_list_split[5]+"\t"+imp_list_split[6]+" "+imp_list_split[7]+"\t") not in multiple_imp_dihedrals_list:
			print (renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+imp_list_split[4]+"\t"+imp_list_split[5]+"\t"+imp_list_split[6]+" "+imp_list_split[7]+"\t")
			multiple_imp_dihedrals_list.append(renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+imp_list_split[4]+"\t"+imp_list_split[5]+"\t"+imp_list_split[6]+" "+imp_list_split[7]+"\t")
		improper_rtp += (atom1+"\t"+atom2+"\t"+atom2+"\t"+atom4+"\n")
		m += 1
	print ( " [ impropers ])")
	print ("Enter below impropers in rtp entry under bond_types section\n [ impropers ] ")
	print (improper_rtp)
		
def printing_dihes(dihe_lists):  
	m = 0	
	multiple_dihedrals_list = []
	list_dihe = []
	print ("[dihedrals]")
	while m < len(dihe_lists):
		n = 0
		while n < len(atom_type):
			dihe_list_split = dihe_lists[m].split()
			if dihe_list_split[0] == atom_type[n]:		  
				renamed_diheatom1 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			dihe_list_split = dihe_lists[m].split()
			if dihe_list_split[1] == atom_type[n]:
				renamed_diheatom2 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			dihe_list_split = dihe_lists[m].split()
			if dihe_list_split[2] == atom_type[n]:
				renamed_diheatom3 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			dihe_list_split = dihe_lists[m].split()
			if dihe_list_split[3] == atom_type[n]:
				renamed_diheatom4 = atom_type[n-1]
				break	
			n += 1
		if (renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+dihe_list_split[4]+"\t"+dihe_list_split[5]+"\t"+dihe_list_split[6]+" "+dihe_list_split[7]+"\t") not in multiple_dihedrals_list:
			print(renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+dihe_list_split[4]+"\t"+dihe_list_split[5]+"\t"+dihe_list_split[6]+" "+dihe_list_split[7]+"\t")
			multiple_dihedrals_list.append(renamed_diheatom1+"\t"+renamed_diheatom2+"\t"+renamed_diheatom3+"\t"+renamed_diheatom4+"\t"+dihe_list_split[4]+"\t"+dihe_list_split[5]+"\t"+dihe_list_split[6]+" "+dihe_list_split[7]+"\t") 
		m += 1

def printing_angles(angle_lists):  
	m = 0
	multiple_angles_list = []
	print(" [ angletypes ] ")
	while m < len(angle_lists):
		n = 0
		while n < len(atom_type):
			angle_list_split = angle_lists[m].split()
			if angle_list_split[0] == atom_type[n]:		 
				renamed_angleatom1 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			angle_list_split = angle_lists[m].split()
			if angle_list_split[1] == atom_type[n]:	
				renamed_angleatom2 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			angle_list_split = angle_lists[m].split()
			if angle_list_split[2] == atom_type[n]:
				renamed_angleatom3 = atom_type[n-1]
				break
			n += 1
		if (renamed_angleatom1+"\t"+renamed_angleatom2+"\t"+renamed_angleatom3+"\t"+angle_list_split[3]+"\t"+angle_list_split[4]+" "+angle_list_split[5]+"\t") not in multiple_angles_list:
			print (renamed_angleatom1+"\t"+renamed_angleatom2+"\t"+renamed_angleatom3+"\t"+angle_list_split[3]+"\t"+angle_list_split[4]+" "+angle_list_split[5]+"\t")
			multiple_angles_list.append(renamed_angleatom1+"\t"+renamed_angleatom2+"\t"+renamed_angleatom3+"\t"+angle_list_split[3]+"\t"+angle_list_split[4]+" "+angle_list_split[5]+"\t")
		m += 1

def printing_bonds(bond_lists):
	m = 0
	multiple_bonds_list = []
	print(" [ bondtypes ] ")
	while m < len(bond_lists):
		n = 0
		while n < len(atom_type):
			bond_list_split = bond_lists[m].split()
			if bond_list_split[0] == atom_type[n]:
				renamed_bondatom1 = atom_type[n-1]
				break
			n += 1
		n = 0
		while n < len(atom_type):
			bond_list_split = bond_lists[m].split()
			if bond_list_split[1] == atom_type[n]:
				renamed_bondatom2 = atom_type[n-1]
				break
			n += 1
		if (renamed_bondatom1+"\t"+renamed_bondatom2+"\t"+bond_list_split[2]+"\t"+bond_list_split[3]+" "+bond_list_split[4]+"\t") not in multiple_bonds_list:
			print(renamed_bondatom1+"\t"+renamed_bondatom2+"\t"+bond_list_split[2]+"\t"+bond_list_split[3]+" "+bond_list_split[4]+"\t")
			multiple_bonds_list.append(renamed_bondatom1+"\t"+renamed_bondatom2+"\t"+bond_list_split[2]+"\t"+bond_list_split[3]+" "+bond_list_split[4]+"\t")
		m += 1

make_list("bonds")
make_list("angles")
make_list("dihedrals")

try:
	make_list("impropers")
except:
	None
