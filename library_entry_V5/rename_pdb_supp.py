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
		return (pdb.find_hydrogens(lines_list,hydro_dict,heavy_dict))
		
	def find_hydrogens(lines_list,hydro_dict,heavy_dict):
		n = 0
		heavy_atom_conect_list = []
		finished_list = []
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
		renamed_list = []
		while m < len(heavy_atom_conect_list):  #renaming atom names for hydrogens
			heavy_atom = heavy_atom_conect_list[m]
			n = 0
			count_check = 0
			while n < (len(lines_list)):
				if heavy_atom in lines_list[n]:
					if count_list[m] > 1:
						count_check += 1
						renamed_list.append([lines_list[n][0] + "  H" + str(heavy_dict[heavy_atom][1:]) + str(count_check)])
					else:
						renamed_list.append([lines_list[n][0] + "  H" + str(heavy_dict[heavy_atom][1:]) + str(1)])
				n += 1
			m += 1
		return (renamed_list)
		
	def write_renamed(filename,renamed_list):  #writing the data to a list
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		n = 0
		renamed_lines = []
		for line in read_lines:
			atmhtm = line[0:6]
			check_atmhtm = atmhtm.split()
			if check_atmhtm[0] == "ATOM" or check_atmhtm[0] == "HETATM":
				atom_number = str(int(line[6:11]))
				residue = str(line[16:20])
				atom_name = str(line[11:16].split()[0])
				m = 0
				while m < len(renamed_list):
					if atom_number == renamed_list[m][0].split()[0]:
						line = line.replace(line[11:16],abs(len(line[11:16])-len(renamed_list[m][0].split()[1])) * " " + renamed_list[m][0].split()[1])
					m += 1
			renamed_lines.append(line)
		outfile = open(filename[:-24] + "_renamed.pdb","w")
		for line in renamed_lines:
			outfile.write(line)
		outfile.close()
		
	def rename_heavy_atoms(filename): #renaming heavy atoms
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		n = 0
		renamed_lines = []
		for line in read_lines:
			atmhtm = line[0:6]
			check_atmhtm = atmhtm.split()
			if len(line) > 2 and (check_atmhtm[0] == "ATOM" or check_atmhtm[0] == "HETATM"):
				atom_number = str(int(line[6:11]))
				residue = str(line[16:20])
				atom_name = str(line[11:16].split()[0])
				atom_name_from_last_entry = str(line[76:78].split()[0])
				if atom_name_from_last_entry != "H":
					length_of_entry = len(line[11:16])-len(atom_name_from_last_entry + str(n+1))
					line = line.replace(line[11:16],str(abs(length_of_entry) * " " ) + atom_name_from_last_entry + str(n+1))
			renamed_lines.append(line)
			n += 1
		outfile = open(filename[:-4] + "_heavy_atoms_renamed.pdb","w")
		for line in renamed_lines:
			outfile.write(line)
		outfile.close()