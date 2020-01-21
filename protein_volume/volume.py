import sys
import volume_supp as vs
import atom_det as dt
import time
import numpy as np
from multiprocessing import Pool
import multiprocessing

import os

try:
	os.system("rm volume_data.txt")
except:
	None

#inputs
try:
	default_set = str(sys.argv[2])
	if default_set == str(0):
		probe_size = 5
		surface_probe_diameter = 1.4
		threads = multiprocessing.cpu_count()
except:
	probe_size = float(input("Grid spacing in angstrom (0 for default):   "))
	if probe_size == 0:
		probe_size = 5
	
	surface_probe_diameter = float(input("Surface probe's diameter in angstrom (0 for default):   "))
	if surface_probe_diameter == 0:
		surface_probe_diameter = 1.4
	
	threads = int(input("Number of threads (0 for all) :   "))
	if threads == 0:
		threads = multiprocessing.cpu_count()

#Default index size is NULL, as it finds the size automatically
index_size = 10 # #1.0

filename = sys.argv[1]

radius = dt.details.van_radius() #atom radius data

#protein_file_list
x_np_list,y_np_list,z_np_list,element_np_list = vs.pdb.protein_data_extract(filename)

#grid file list
grid_np_list_x,grid_np_list_y,grid_np_list_z,index_list,ref_dict = vs.pdb.grid(x_np_list,y_np_list,z_np_list,element_np_list,probe_size,surface_probe_diameter,index_size)

#outfile
outfile_volume = open("volume_data.txt","a")
total_grid_points = int(len(grid_np_list_x))
print (str(total_grid_points) + " grid points")

'''
n = 1
for listt in index_list:
	checkx = []
	checky = []
	checkz = []
	for entry in listt:
		#print (entry[0])
		checkx.append(entry.split(",")[0])
		checky.append(entry.split(",")[1])
		checkz.append(entry.split(",")[2])
	vs.pdb.write_to_file(checkx,checky,checkz,"index" +str(n)+".pdb")
	n += 1'''
	
outfile_volume.write(str(total_grid_points) + " grid points\n")

print ("Done step 1/6")

#all point sets
protein_points_set = []
probe_points_set = []
void_points_set = []
protein_inverse_points_set = []



def make_set_list(list,name,set_name):
	n = 0
	while n < len(list[0]):
		if list[0][n] != None:
			items = list[0][n].split()
			m = 0
			while m < len(items):
				if items[m] not in set_name:
					set_name.append(items[m])
				m += 1
		n += 1
	return (set_name)
	outfile = open(name[:-4] + ".txt","w")
	n = 0
	while n < len(set_name):
		outfile.write(str(set_name[n]) + "\n")
		n += 1
	outfile.close()
	print(len(set_name),name)
	outfile_volume.write(str(len(set_name)) + "   " +  name + "\n")
	
def void_volume2(protein_points):
	m = 0
	prot_x,prot_y,prot_z = unpack_xyz(protein_points)
	void_list = []
	while m < len(grid_np_list_x):
		check_line = str(grid_np_list_x[m]) + "," + str(grid_np_list_y[m]) + "," + str(grid_np_list_z[m])
		if check_line not in protein_points:
			x_axis = np.power((prot_x-float(grid_np_list_x[m])),2)
			y_axis = np.power((prot_y-float(grid_np_list_y[m])),2)
			z_axis = np.power((prot_z-float(grid_np_list_z[m])),2)
			distance_to_atoms = (np.sqrt(x_axis+y_axis+z_axis))
			distance_check1 = (distance_to_atoms >= (surface_probe_diameter/2)) 
			distance_check2 = (distance_to_atoms <= float((10.0) + (surface_probe_diameter/2)))
			if np.all(distance_check2):# and np.all(distance_check2):
				#print (distance_check)
				void_list.append(check_line)
			#print (distance_to_atoms,distance_check)
		m += 1
	print (len(void_list),1)
	'''
			n = 0
			count = 0
			while n < len(x_axis):
				if distance_to_atoms[n] >= (surface_probe_diameter/2):
					count += 1
				else:
					break
				n += 1
			if count == len(x_axis):
				return check_line'''
				
def multiprocessing():				
	if __name__ == '__main__':
		p = Pool(threads)

		protein_points = []
		protein_points.append(p.map(protein_volume_calc, range(len(x_np_list))))
		protein_points_list = make_set_list(protein_points,"protein_points_set",protein_points_set)
		void_volume2(protein_points_list)
		time.sleep(0.1)
		print ("Done step 2/6")
		protein_inverse_points = []
		protein_inverse_points.append(p.map(protein_inverse, range(len(grid_np_list_x))))
		make_set_list(protein_inverse_points,"protein_inverse_points_set",protein_inverse_points_set)
		time.sleep(0.1)
		print ("Done step 3/6")
		probe_points = []
		protein_inverse_points_infile = open("protein_inverse_points.txt","r").read().split()
		probe_points.append(p.map(surface_probe_points, range(len(protein_inverse_points_infile))))
		make_set_list(probe_points,"probe_points_set",probe_points_set)
		time.sleep(0.1)
		print ("Done step 4/6")
		void_points = []
		void_points.append(p.map(void_volume,range(len(grid_np_list_x))))
		make_set_list(void_points,"void_points_set",void_points_set)
		time.sleep(0.1)
		print ("Done step 5/6")
		
def unpack_xyz(input_list):
	x_list = []
	y_list = []
	z_list = []
	for entry in input_list:
		x_list.append(float(entry.split(",")[0]))
		y_list.append(float(entry.split(",")[1]))
		z_list.append(float(entry.split(",")[2]))
	return (np.array(x_list),np.array(y_list),np.array(z_list))
	
def protein_volume_calc(m):
	index_list,ref_dict
	
	entryx = x_np_list[m]
	entryy = y_np_list[m]
	entryz = z_np_list[m]
	
	if probe_size < 0.3:
		error_distance = index_size/2 + 0.3  + probe_size
	else:
		error_distance = index_size/2  + probe_size
			
	to_check_index = []
	for index in ref_dict:
		xc,yc,zc = index.split(",")
		x_parm1,x_parm2 = float(xc) + error_distance,float(xc) - error_distance
		y_parm1,y_parm2 = float(yc) + error_distance,float(yc) - error_distance
		z_parm1,z_parm2 = float(zc) + error_distance,float(zc) - error_distance
		if (entryx <= x_parm1 and entryx >= x_parm2) and (entryy <= y_parm1 and entryy >= y_parm2) and (entryz <= z_parm1 and entryz >= z_parm2):
			to_check_index.append(int(ref_dict[index]))
	
	protein_points = ""
	for values in to_check_index:
		grix_x,grid_y,grid_z = unpack_xyz(index_list[values])
		x_axis = np.power((grix_x-x_np_list[m]),2)
		y_axis = np.power((grid_y-y_np_list[m]),2)
		z_axis = np.power((grid_z-z_np_list[m]),2)
		distance_to_atoms = (np.sqrt(x_axis+y_axis+z_axis))
		n = 0
		while n < len(distance_to_atoms):
			if distance_to_atoms[n] <= (float(radius[element_np_list[m]])) * 0.01:
				protein_points += (str(grix_x[n]) + "," + str(grid_y[n]) + "," + str(grid_z[n]) + "\n")
			else:
				None
			n += 1
	return protein_points

def file_open(filename,m):
	open_file = open(filename,"r")
	file_split = open_file.read().split()[m]
	open_file.close()
	x = []
	y = []
	z = []
	coordinates = file_split.split(",")
	n = 0
	while n < len(coordinates):
		x.append(float(coordinates[0]))
		y.append(float(coordinates[1]))
		z.append(float(coordinates[2]))
		n += 1
	return x,y,z
	
def surface_probe_points(m):
	surface_points = ""
	x,y,z = file_open("protein_inverse_points.txt",m)
	x_axis = np.power(x_np_list-(float(x[0])),2)
	y_axis = np.power(y_np_list-(float(y[0])),2)
	z_axis = np.power(z_np_list-(float(z[0])),2)
	distance_to_atoms = (np.sqrt(x_axis+y_axis+z_axis))
	n = 0
	count = 0
	while n < len(x_axis):
		if float(distance_to_atoms[n]) > float((2.0) + (surface_probe_diameter/2)):
			count += 1
		else:
			break
		n += 1
	if count == len(x_axis):
		surface_points += (str(x[0]) + "," + str(y[0]) + "," + str(z[0]) + "\n")
		return surface_points
		
	
				
def protein_inverse(m):
	count = 0
	points = ""
	protein_points_infile = open("protein_points.txt","r").read().split()
	check_line = str(grid_np_list_x[m]) + "," + str(grid_np_list_y[m]) + "," + str(grid_np_list_z[m])
	#print (grid_np_list_x[0],protein_points_infile[0])
	if check_line not in protein_points_infile:
		points += check_line
	return points

def make_np_from_file(filename):
	open_file = open(filename,"r")
	file_split = open_file.read().split()
	open_file.close()
	x = []
	y = []
	z = []
	surface_points = ""
	n = 0
	while n < len(file_split):
		coordinates = file_split[n].split(",")
		x.append(float(coordinates[0]))
		y.append(float(coordinates[1]))
		z.append(float(coordinates[2]))
		n += 1
	x_np = np.array(x)
	y_np = np.array(y)
	z_np = np.array(z)
	return x_np,y_np,z_np

def void_volume(m):
	protein_points_infile = open("protein_points.txt","r").read().split()
	probe_points_infile = open("probe_points.txt","r").read().split()
	check_line = str(grid_np_list_x[m]) + "," + str(grid_np_list_y[m]) + "," + str(grid_np_list_z[m])
	if check_line not in protein_points_infile:
		if check_line not in probe_points_infile:
			x,y,z = make_np_from_file("protein_points.txt")
			x_axis = np.power((x-float(grid_np_list_x[m])),2)
			y_axis = np.power((y-float(grid_np_list_y[m])),2)
			z_axis = np.power((z-float(grid_np_list_z[m])),2)
			distance_to_atoms = (np.sqrt(x_axis+y_axis+z_axis))
			n = 0
			count = 0
			while n < len(x_axis):
				if distance_to_atoms[n] >= (surface_probe_diameter/2):
					count += 1
				else:
					break
				n += 1
			if count == len(x_axis):
				return check_line


	
multiprocessing()

vs.pdb.divided_points("protein_points.txt","protein_grid.pdb")
vs.pdb.divided_points("void_points.txt","void_grid.pdb")
vs.pdb.divided_points("probe_points.txt","probe_grid.pdb")

print ("Done step 6/6")

protein_infile = open("protein_points.txt","r").read().split()
void_infile = open("void_points.txt","r").read().split()
	

void_volume = np.power(probe_size,3) * len(void_infile)
protein_volume = np.power(probe_size,3) * len(protein_infile) #cubic
print ("\n\n\n" + str(protein_volume) + " A^3 protein volume")
print (str(void_volume) + " A^3 void volume")
total_volume = protein_volume + void_volume
print ("Total volume = " + str(total_volume) + " A^3 void volume")
print ("Packing efficiency = " +	 str((protein_volume/total_volume)*100) + " %")
print ("Mass = " + str(vs.pdb.mass(element_np_list)))
print ("Density ", vs.pdb.mass(element_np_list)/total_volume)

outfile_volume.write("\n\n\nProtein volume = " + str(protein_volume) + " A^3 \n")
outfile_volume.write("Void volume = " + str(void_volume) + " A^3 \n")
outfile_volume.write("Total volume = " + str(total_volume) + " A^3 \n")
outfile_volume.write("Packing efficiency = " +	 str((protein_volume/total_volume)*100) + " %\n")
outfile_volume.write("Density " +  str(vs.pdb.mass(element_np_list)/total_volume))