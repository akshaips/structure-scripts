import hdb_entry_supp as he
import sys
import os

filename = sys.argv[1]
residue_name = sys.argv[2]

first_conect,second_list = he.pdb.conect(filename)
second_set = []
n = 0
while n < len(second_list):
	if second_list[n] not in second_set:
		second_set.append(second_list[n])
	n += 1
	
def third_conect(filename,second_line,first_conect):
		hydro_dict,heavy_dict = he.pdb.hydro(filename)
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		third_list = second_line
		entry_check = 0
		for line in read_lines:
			read_split = line.split()
			if read_split[0] == "CONECT":
				n = 0
				while n < len(first_conect):
					if read_split[1] in heavy_dict and entry_check == 0:
						if heavy_dict[read_split[1]] == second_line.split()[2]:
							m = 0
							while m < len(read_split):
								if m > 2:
									if  read_split[m] in heavy_dict and heavy_dict[read_split[m]] not in second_line.split() and entry_check == 0:
										third_list = (second_line + " " + heavy_dict[read_split[m]])
										check_line = second_line + " " + heavy_dict[read_split[m]]
										entry_check += 1
									if read_split[m] in heavy_dict and heavy_dict[read_split[m]] not in second_line.split() and entry_check == 1 \
										and heavy_dict[read_split[m]] not in third_list.split():
										third_list = (check_line + " " + heavy_dict[read_split[m]])
										check_line2 = check_line + " " + heavy_dict[read_split[m]]
										entry_check += 1
									if read_split[m] in heavy_dict and heavy_dict[read_split[m]] not in second_line.split() and entry_check == 2 \
										and heavy_dict[read_split[m]] not in third_list.split():
										third_list = (check_line2 + " " + heavy_dict[read_split[m]])
										entry_check += 1
										break
								m += 1
					n += 1
		return (third_list)
		
def last_conect(filename,second_line,first_conect):
		hydro_dict,heavy_dict = he.pdb.hydro(filename)
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		third_list = second_line
		entry_check = 0
		for line in read_lines:
			read_split = line.split()
			if read_split[0] == "CONECT":
				n = 0
				while n < len(first_conect):
					if read_split[1] in heavy_dict and entry_check == 0:
						if heavy_dict[read_split[1]] == second_line.split()[3]:
							m = 0
							while m < len(read_split):
								if m > 2:
									if  read_split[m] in heavy_dict and heavy_dict[read_split[m]] not in second_line.split() and entry_check == 0:
										third_list = (second_line + " " + heavy_dict[read_split[m]])
										check_line = second_line + " " + heavy_dict[read_split[m]]
										entry_check += 1
								m += 1
					n += 1
		return (third_list)


third_list = []
n = 0
while n < len(second_set):
	third_list.append(third_conect(filename,second_set[n],first_conect),)
	n += 1


third_set = []
n = 0
while n < len(third_list):
	if third_list not in third_set and len(third_list) > 0:
		third_set.append(third_list[n])
	n += 1
	
fourth_list = []
n = 0
while n < len(third_set):
	if len(third_set[n].split()) < 5:
		fourth_list.append(last_conect(filename,third_set[n],first_conect))
	else:
		fourth_list.append(third_set[n])
	n += 1

print ("Enter in aminoacids.hdb and include the atom type")
print (residue_name,len(fourth_list))
n = 0
while n < len(fourth_list):
	print (str(fourth_list[n].split()[0]) + " # " + str(fourth_list[n][1:]))
	n += 1