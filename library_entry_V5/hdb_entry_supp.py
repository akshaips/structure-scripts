class pdb():
	#use  pdbopdbqt.pdb.value(filename,variable)
	def __init__(self):
		print ("use  pdbopdbqt.pdb.value(filename,variable)")
	def hydro(filename): #making hydrogen and heavy atom dict
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		n = 0
		hydro_dict = {}
		heavy_dict = {}
		for line in read_lines:
			atmhtm = line[0:6]
			check_atmhtm = atmhtm.split()
			if len(line) > 2 and (check_atmhtm[0] == "ATOM" or check_atmhtm[0] == "HETATM"):
				atom_number = str(int(line[6:11]))
				residue = str(line[16:20])
				atom_name = str(line[11:16].split()[0])
				if line[76:78].split()[0] == "H":
					hydro_dict[atom_number] = atom_name
				else:
					heavy_dict[atom_number] = atom_name
				n += 1
		return (hydro_dict,heavy_dict)
		
	def conect(filename): #reading conect for hydrogens
		hydro_dict,heavy_dict = pdb.hydro(filename)
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		lines_list = []
		for line in read_lines:
			read_split = line.split()
			if read_split[0] == "CONECT":
				if read_split[1] in hydro_dict:
					lines_list.append(read_split[1:])		
		return (pdb.find_hydrogens(lines_list,hydro_dict,heavy_dict,filename))
		
	def find_hydrogens(lines_list,hydro_dict,heavy_dict,filename):
		n = 0
		heavy_atom_conect_list = []
		first_set = []
		first_conect = []
		while n < len(lines_list): #finding heavy atom corresponding to hydrogen
			m = 0
			line_split = lines_list[n]
			while m < len(lines_list[n]):	
				if line_split[m+1] not in heavy_atom_conect_list:
					heavy_atom_conect_list.append(line_split[m+1])
				m += 2
			n += 1
		count_list = []
		for heavy_atom in heavy_atom_conect_list: #counting number of hydrogens attached to the atom
			n = 0
			count = 0
			while n < (len(lines_list)):
				if heavy_atom in lines_list[n]:
					count += 1
				n += 1
			count_list.append(count)
		m = 0
		while m < len(heavy_atom_conect_list):  #renaming atom names for hydrogens
			heavy_atom = heavy_atom_conect_list[m]
			n = 0
			while n < (len(lines_list)):
				if heavy_atom in lines_list[n]:
					if count_list[m] > 1:
						first_set.append(str(count_list[m]) + " " +hydro_dict[lines_list[n][0]][:-1] +     "  " + str(heavy_dict[heavy_atom]))
					else:
						first_set.append(str(count_list[m]) + " " + hydro_dict[lines_list[n][0]] +  "  " + str(heavy_dict[heavy_atom]))
					first_conect.append(heavy_atom)
				n += 1
			m += 1
		return (first_conect,pdb.second_conect(filename,first_set,first_conect))
		
	def second_conect(filename,first_set,first_conect):
		hydro_dict,heavy_dict = pdb.hydro(filename)
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		lines_list = []
		second_set = []
		for line in read_lines:
			read_split = line.split()
			if read_split[0] == "CONECT":
				n = 0
				while n < len(first_conect):
					if read_split[1] == first_conect[n]:
						m = 0
						entry_check = 0
						while m < len(read_split):
							if m > 1:
								if  entry_check == 0 and read_split[m] in heavy_dict:
									second_set.append(first_set[n] + " " + heavy_dict[read_split[m]])
									break
							m += 1
					n += 1
		return (second_set)
