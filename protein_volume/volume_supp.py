import atom_det as dt
import math
import numpy as np
import volume_supp as vs

pi = math.pi
	
class pdb():
	#use  pdbopdbqt.pdb.value(filename,variable)
	def __init__(self):
		print ("use  pdbopdbqt.pdb.value(filename,variable)")
	def protein_data_extract(filename): #Fetch protein coordinates and atomtype
		file_open = open(filename,"r")
		read_lines = file_open.readlines()
		x_list = []
		y_list = []
		z_list = []
		element_list = []
		for line in read_lines:
			if len(line) > 53:
				atmhtm = line[0:5]
				check_atmhtm = atmhtm.split()
				if check_atmhtm[0] == "ATOM" or check_atmhtm[0] == "HETATM":
						atom_number = int(line[6:11])
						residue = str(line[16:20])
						x = float(line[30:38].split()[0])
						y = float(line[38:46].split()[0])
						z = float(line[46:54].split()[0])
						element = str(line[12:16].split()[0])
						x_list.append(x)
						y_list.append(y)
						z_list.append(z)
						element_list.append(dt.details.atom_type(element))
		x_np_list = np.array(x_list)
		y_np_list = np.array(y_list)
		z_np_list = np.array(z_list)
		element_np_list = np.array(element_list)
		return (x_np_list,y_np_list,z_np_list,element_np_list)

	def extremes(axis,element):
		radius = dt.details.van_radius()
		minimum = np.amin(axis) - (float(radius[element[np.argmin(axis)]]) * 0.01)
		maximum = np.amax(axis) + (float(radius[element[np.argmax(axis)]]) * 0.01)
		return (minimum,maximum)
	
	def grid(x,y,z,element_list,probe_size,surface_probe,index_size):
		grid_list_x = []
		grid_list_y = []
		grid_list_z = []
		x_min,x_max = pdb.extremes(x,element_list)
		y_min,y_max = pdb.extremes(y,element_list)
		z_min,z_max = pdb.extremes(z,element_list)
		x_axis_length = float(abs(x_min)+abs(x_max))
		y_axis_length = float(abs(y_min)+abs(y_max))
		z_axis_length = float(abs(z_min)+abs(z_max))
		list_len = 0
		n = 0
		error_value = surface_probe
		while n < x_axis_length + (error_value*2) + 2:
			x_point = (x_min - (error_value) - 1) + n
			m = 0
			while m < y_axis_length + (error_value*2) + 2:
				y_point = (y_min - (error_value) - 1) + m
				o = 0
				while o < z_axis_length + (error_value*2) + 2:
					z_point = (z_min - (error_value) - 1) + o
					grid_list_x.append(float(x_point))
					grid_list_y.append(float(y_point))
					grid_list_z.append(float(z_point))
					o += probe_size
				m += probe_size
			n += probe_size
		pdb.write_to_file(grid_list_x,grid_list_y,grid_list_z,"Grid_box.pdb")
		grid_np_list_x = np.array(grid_list_x)
		grid_np_list_y = np.array(grid_list_y)
		grid_np_list_z = np.array(grid_list_z)
		index_list,ref_dict = pdb.indexing(x,y,z,grid_np_list_x,grid_np_list_y,grid_np_list_z,probe_size,element_list,index_size)
		return (grid_np_list_x,grid_np_list_y,grid_np_list_z,index_list,ref_dict)
		
	def indexing(x,y,z,grid_np_list_x,grid_np_list_y,grid_np_list_z,probe_size,element_list,index_size):
	
		
		x_min,x_max = pdb.extremes(x,element_list)
		y_min,y_max = pdb.extremes(y,element_list)
		z_min,z_max = pdb.extremes(z,element_list)
			
		uniquex, countsx = np.unique(grid_np_list_x, return_counts=True)
		uniquey, countsy = np.unique(grid_np_list_y, return_counts=True)
		uniquez, countsz = np.unique(grid_np_list_z, return_counts=True)
		x_points = int(np.sqrt((countsy[0]*countsz[0])/countsx[0]))
		y_points = int(np.sqrt((countsx[0]*countsz[0])/countsy[0]))
		z_points = int(np.sqrt((countsx[0]*countsy[0])/countsz[0]))
		x_count = (np.ceil(float(x_points) * float(probe_size)/index_size))
		y_count = (np.ceil(float(y_points) * float(probe_size)/index_size))
		z_count = (np.ceil(float(z_points) * float(probe_size)/index_size))
		total_segmentation = int(x_count * y_count * z_count)
		index_list = [[] for entry in range(total_segmentation)]
		
		ref_dict = {}
		n = 0
		x_mid = x_min + index_size/2
		while x_mid < x_max + (np.ceil(float(x_points) * float(probe_size)//index_size)):
			y_mid = y_min + index_size/2
			while y_mid < y_max + (np.ceil(float(y_points) * float(probe_size)//index_size)):
				z_mid = z_min + index_size/2
				while z_mid < z_max + (np.ceil(float(z_points) * float(probe_size)//index_size)):
					ref_dict[str(x_mid)+","+str(y_mid)+","+str(z_mid)] = str(n)
					n += 1
					z_mid += index_size
				y_mid += index_size
			x_mid += index_size
			
		if probe_size < 0.3:
			error_distance = index_size/2 + 0.3  + probe_size
		else:
			error_distance = index_size/2  + probe_size
		for entryx,entryy,entryz in zip(grid_np_list_x,grid_np_list_y,grid_np_list_z):
			for index in ref_dict:
				xc,yc,zc = index.split(",")
				x_parm1,x_parm2 = float(xc) + error_distance,float(xc) - error_distance
				y_parm1,y_parm2 = float(yc) + error_distance,float(yc) - error_distance
				z_parm1,z_parm2 = float(zc) + error_distance,float(zc) - error_distance
				if (entryx <= x_parm1 and entryx >= x_parm2) and (entryy <= y_parm1 and entryy >= y_parm2) and (entryz <= z_parm1 and entryz >= z_parm2):
					index_list[int(ref_dict[index])].append(str(entryx) +","+ str(entryy) +","+ str(entryz))
					break
		return (index_list,ref_dict)
		
	def divided_points(infile,filename):
		input_file = open(infile,"r").read().split()
		n = 0
		x = []
		y = []
		z = []
		while n < len(input_file):
			coordinates = input_file[n].split(",")
			x.append(coordinates[0])
			y.append(coordinates[1])
			z.append(coordinates[2])
			n += 1
		pdb.write_to_file(x,y,z,filename)
		
	def write_to_file(x,y,z,filename): #write grid to pdb file and make a new pdb
		output = open(filename,"w")
		writing = ""
		n = 0
		while n < len(x):
			x_a = str(x[n])[:6]
			y_a = str(y[n])[:6]
			z_a = str(z[n])[:6]
			if len(x_a) < 6:
				x_a += (6 - len(x_a)) * "0"
			if len(y_a) < 6:
				y_a += (6 - len(y_a)) * "0"
			if len(z_a) < 6:
				z_a += (6 - len(z_a)) * "0"
			writing += ("ATOM      1  H   GRD     1      " + x_a + "  " + y_a + "  " + z_a + "  1.00  0.00           H\n")
			n += 1
		output.write(writing)
		
	def mass(element_np_list):
		mass = dt.details.mass()
		total_mass = 0
		for entry in element_np_list:
			total_mass += (float(mass[entry]))
		return total_mass
		
