#!/usr/bin/env python3

import os
import glob
import sys
from multiprocessing import Pool
import multiprocessing

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#" set path for the respective files from mgl tools directory  "
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set_path = "/usr/local/MGLTools-1.5.6/" # change path in this line

# DO NOT EDIT
prepare_gpf_path = set_path + "MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py"
prepare_dpf_path = set_path + "MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py"
prepare_receptor_path = set_path + "MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py"
pythonsh_path = set_path + "bin/pythonsh"


#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#" Used to convert pdb to pdbqt, if already pdbqt, remove paralleling "
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def to_pdbqt(pdb):
    os.system(pythonsh_path + " " + prepare_receptor_path + " -r " + pdb)

	
#""""""""""""""""""""""""""""""""""""""""""""""
#"  Making of gpf and dpf files for docking   "
#""""""""""""""""""""""""""""""""""""""""""""""



def make_grid_file(coordinates_1,coordinates_2,coordinates_3,name):
    os.system(pythonsh_path + " " + prepare_gpf_path + " -l " + ligand_name + " -r " + name + " -p gridcenter='" + str(coordinates_1) + "," + str(coordinates_2) + "," + str(coordinates_3) + "'" + " -p npts='" + npts_1 + "," + npts_2 + "," + npts_3 + "'" + " -p spacing=" + grid_spacing)

def make_dock_file(name):
    os.system(pythonsh_path + " " + prepare_dpf_path + " -l " + ligand_name + " -r " + name + " -o " + name[:-6] + ".dpf -p ga_run=" + ga_run)



#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#" Finding the center of the residues by taking alpha-carbon as the point "
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def corr(pdbqt,grid_residues_file):
    open_grid_file = open(grid_residues_file,"r").readlines()
    file_open = open(pdbqt,"r")
    read_lines = file_open.readlines()
    x = 0
    y = 0
    z = 0
    number_of_residues = 0
    for lines in open_grid_file:
        if len(lines.split()) > 2:
            number_of_residues += 1
            grid_file_split = lines.split()
            n = 0
            for pdbqt_line in read_lines:
                if len(pdbqt_line) > 53:
                    atmhtm = pdbqt_line[0:5]
                    check_atmhtm = atmhtm.split()
                    residue = str(pdbqt_line[16:20].split()[0])
                    atom = str(pdbqt_line[12:16].split()[0])
                    resid = str(pdbqt_line[22:26].split()[0])
                    if (check_atmhtm[0] == "ATOM" or check_atmhtm[0] == "HETATM") and residue == grid_file_split[0] and resid == grid_file_split[1] and atom == grid_file_split[2]:
                        atom_number = int(pdbqt_line[6:11])
                        x_ = pdbqt_line[30:38].split()
                        y_ = pdbqt_line[38:46].split()
                        z_ = pdbqt_line[46:54].split()
                        x += float(x_[0])
                        y += float(y_[0])
                        z += float(z_[0])
                n += 1
    return (x/number_of_residues,y/number_of_residues,z/number_of_residues)
    
def atom_corr(pdbqt): 
    if True:
        if pdbqt != ligand_name:
            coordinates_1,coordinates_2,coordinates_3 = corr(pdbqt,grid_residues)
            make_grid_file(coordinates_1,coordinates_2,coordinates_3,pdbqt)
            make_dock_file(pdbqt)
			
#"""""""""""""""""""""""""""
#" For paralleling the run "
#"""""""""""""""""""""""""""

pdb_s = glob.glob("*.pdb")
pdbqt_s = glob.glob("*.pdbqt")
	
def paralleling(program):
    if __name__ == '__main__':
        p = Pool(num_threads)
        if program == "conversion":
            p.map(to_pdbqt, pdb_s)
        else:
            p.map(atom_corr, pdbqt_s)
			
#"""""""""""""""""""""""""""""""""""""""
#" All the inputs are received here    "
#"""""""""""""""""""""""""""""""""""""""
			
if len(sys.argv) <= 7:
	print ("\n\nUSAGE:\n\npython make_gpf_dpf.py ligand_name residues_file_name npts1 npts2 npts3 grid_spacing GA_runs \n\n\teg:\n\npython make_gpf_dpf.py ligand.pdbqt residues_filename.txt 60 60 60 0.237 50 \n\n")
	print("*Important  \nresidues_filename.txt should contain 'residue residue_number atomtype' \neg: GLN 97 CA\n    SER 86 OG")
else:
	ligand_name = sys.argv[1]
	grid_residues = sys.argv[2]
	npts_1 = sys.argv[3]
	npts_2 = sys.argv[4]
	npts_3 = sys.argv[5]
	grid_spacing = sys.argv[6]
	ga_run = sys.argv[7]
    
	'''ligand_name = input("Ligand pdbqt filename" : )
	residue1 = input("Residue 1: ")
	residue1_num = input("Residue_1 number: ")
	atom_type1 = input("Atom type: ")
	residue2 = input("Residue 2: ")
	residue2_num = input("Residue_2 number: ")
	atom_type2 = input("Atom type: ")
	residue3 = input("Residue 3: ")
	residue3_num = input("Residue_3 number: ")
	atom_type3 = input("Atom type: ")
	npts_1 = input("Enter first npts point:   ")
	npts_2 = input("Enter second npts point:   ")
	npts_3 = input("Enter third npts point:   ")
	grid_spacing = input("Enter grid spacing:   ")
	ga_run = input("Enter number of structures:   ")'''
	
	num_threads = int(input("Number of threads to be used ('0' to use all the threads) : "))
	if num_threads == 0:
		num_threads = multiprocessing.cpu_count()  #change this to number of threads the program should run in

	paralleling("conversion") #convert pdb to pdbqt
	paralleling("dock_files") #make dpf and gpf files
