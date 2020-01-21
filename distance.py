#!/usr/bin/env python3

import os
import glob
import sys
import numpy as np

#'''''''''''''''''''''''''''''''''''''''''
#'Extracting coordinates if pdb or pdbqt '
#'''''''''''''''''''''''''''''''''''''''''

def for_pdbqt(pdbqt_split,input_atom,input_number,list_num):
	n = 0
	while n < len(pdbqt_split):
		if n+4 < len(pdbqt_split):
			if pdbqt_split[n] == input_atom and pdbqt_split[n+3] == input_number:
				if list_num == 1:
					list1.append(pdbqt_split[n+4] + " " + pdbqt_split[n+5] + " " + pdbqt_split[n+6]+ " " )
				if list_num == 2:
					list2.append(pdbqt_split[n+4]+ " " +pdbqt_split[n+5]+ " " +pdbqt_split[n+6]+ " " )
			elif pdbqt_split[n] == input_atom and pdbqt_split[n+2] == input_number:
				if list_num == 1:
					list1.append(pdbqt_split[n+3] + " " + pdbqt_split[n+4] + " " + pdbqt_split[n+5]+ " " )
				if list_num == 2:
					list2.append(pdbqt_split[n+3]+ " " +pdbqt_split[n+4]+ " " +pdbqt_split[n+5]+ " " )
		n += 1

#'''''''''''''''''''''''''''''''
#'Extracting coordinates if dlg'
#'''''''''''''''''''''''''''''''

def for_dlg(dlg_split,input_atom,input_number,list_num):
	n = 0
	while n < len(dlg_split):
		splitted = dlg_split[n]
		if splitted[0:6] == "DOCKED":
			split_split = splitted.split()
			if len(input_number) == 1:
				if splitted[17:19] == " " + input_number and split_split[3] == input_atom:
					if list_num == 1:
						list1.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
					if list_num == 2:
						list2.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
			if len(input_number) == 2:
				if splitted[17:19] == input_number and split_split[3] == input_atom:
					if list_num == 1:
						list1.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
					if list_num == 2:
						list2.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
			if len(input_number) == 3:
				if splitted[16:19] == input_number and split_split[3] == input_atom:
					if list_num == 1:
						list1.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
					if list_num == 2:
						list2.append(splitted[39:47]+ " " +splitted[47:55]+ " " +splitted[55:63]+ " " )
				
		n += 1
		
		
#'''''''''''''''''''''''''''''''
#'Extracting coordinates if gro'
#'''''''''''''''''''''''''''''''
		
def for_gro(gro_split,input_atom,input_number,list_num):
	n = 0
	while n < len(gro_split):
		if gro_split[n] == input_atom:
			if gro_split[n-1][:-3] == input_number:
				if list_num == 1:
					list1.append(str(float(gro_split[n+2])*10)+ " " +str(float(gro_split[n+3])*10)+ " " +str(float(gro_split[n+4])*10)+ " " )
				if list_num == 2:
					list2.append(str(float(gro_split[n+2])*10)+ " " +str(float(gro_split[n+3])*10)+ " " +str(float(gro_split[n+4])*10)+ " " )
				
		n += 1
		
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#'Opening the files and sending to respective function to extract coordinates'
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def file_read():
	if input_file1[-6:] == ".pdbqt" or input_file1[-4:] == ".pdb":
		first = for_pdbqt(pdbqt_split1,input_atom1,input_number1,1)
	elif input_file1[-4:] == ".dlg":
		first = for_dlg(dlg_split1,input_atom1,input_number1,1)
	else:
		first = for_gro(gro_split1,input_atom1,input_number1,1)

	if input_file2[-6:] == ".pdbqt" or input_file2[-4:] == ".pdb":
		second = for_pdbqt(pdbqt_split2,input_atom2,input_number2,2)
	elif input_file2[-4:] == ".dlg":
		second = for_dlg(dlg_split2,input_atom2,input_number2,2)
	else:
		second = for_gro(gro_split2,input_atom2,input_number2,2)
		
	list_making()

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#'Making equal size list of coordinates to find all the angles'
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def list_making():
	list_len = [len(list1),len(list2)]
	angle_num = sorted(list_len)
	list1_string = ""
	list2_string = ""

	if len(list1) != angle_num[-1]:
		n = 1
		while n < angle_num[-1]:
			list1.append(list1[0])
			n += 1
	
	if len(list2) != angle_num[-1]:
		n = 1
		while n < angle_num[-1]:
			list2.append(list2[0])
			n += 1
	
	for each1 in list1:
		list1_string += each1
	for each2 in list2:
		list2_string += each2


	distance_find(list1_string,list2_string)
			
#''''''''''''''''''''''''''''''''''''''''''''''''''
#' Finding distance and ouput is written to a file'
#''''''''''''''''''''''''''''''''''''''''''''''''''

def distance_find(list1_string,list2_string):
	list1_split = list1_string.split()
	list2_split = list2_string.split()
	n = 0
	m = 0
	output = open(output_filename, "w")
	print ("\n" + output_filename + "\n")
	while n < len(list1):
		distance = ((float(list1_split[m]) - float(list2_split[m]))**2 + (float(list1_split[m+1]) - float(list2_split[m+1]))**2 + (float(list1_split[m+2]) - float(list2_split[m+2]))**2)**(1/2)
		n += 1
		m += 3
		output.write(str(distance) + "\n")
		print (distance)

#''''''''''''''''''
#' all inputs     '
#''''''''''''''''''
if len(sys.argv) <= 7 :
	print ("\n \nUSAGE = python angle.py file_name atom_type1 atom_number1 file_name atom_type2 atom_number2 output_filename\n\n or \n\npython angle.py test.pdb CA 156 test.gro CB 130 test_distance.txt\n \n \nUse pdb/gro/dlg/pdbqt")
else:
	input_file1 = sys.argv[1]
	input_atom1 = sys.argv[2]
	input_number1 = sys.argv[3]
	input_file2 = sys.argv[4]
	input_atom2 = sys.argv[5]
	input_number2 = sys.argv[6]
	output_filename = sys.argv[7]

	#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	#' check whether inputs are pdb,pdbqt,dlg or gro and assigning filename to variables'
	#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	if input_file1[-6:] == ".pdbqt" or input_file1[-4:] == ".pdb":
		pdbqt_open = open(input_file1,"r").read()
		pdbqt_split1 = pdbqt_open.split()
	elif input_file1[-4:] ==  ".dlg":
		dlg_open = open(input_file1,"r")
		dlg_split1 = dlg_open.readlines()
	elif input_file1[-4:] == ".gro":
		gro_open = open(input_file1,"r").read()
		gro_split1 = gro_open.split()
		
	if input_file2[-6:] == ".pdbqt" or input_file2[-4:] == ".pdb":
		pdbqt_open = open(input_file2,"r").read()
		pdbqt_split2 = pdbqt_open.split()
	elif input_file2[-4:] == ".dlg":
		dlg_open = open(input_file2,"r")
		dlg_split2 = dlg_open.readlines()
	elif input_file2[-4:] == ".gro":
		gro_open = open(input_file2,"r").read()
		gro_split2 = gro_open.split()

	#''''''''''''''''''''''''''''''''''''''
	#'Global list for to store coordinates'
	#''''''''''''''''''''''''''''''''''''''

	list1 = []
	list2 = []
	file_read()
