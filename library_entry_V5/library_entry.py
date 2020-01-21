#!/usr/bin/env python3

import os
import sys
import parmed as pmd

print ("Make sure CONECT entries are present in the ligand")

print ("\n\n\nArgument 1 has to be ligand PDB file with connect entries")
print ("Argument 2 has to be residue name")
print ("Argument 3 is optional if topology file is available\n\n\n")

#path = os.path.abspath(__file__)[0:-len(sys.argv[0])].split()[0]
path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
print (path)


ligand_file = sys.argv[1]
ligand_name = sys.argv[2]

if len(sys.argv) > 3:
    topology_file = sys.argv[3]
else:
    topology_file = "NEGATIVE"
    
if ligand_file[-4:] == "mol2":
    file_base_name = ligand_file[:-5]
    file_type = ".mol2"
elif ligand_file[-4:] == ".pdb":
    file_base_name = ligand_file[:-4]
    file_type = ".pdb"
else:
    print ("Only mol2 and pdb formats are accepted")
    exit()

def renaming_ligand(): ###Function to rename atom names in the ligand file
    rename_ligand = input("Rename ligand (y/n):   ")
    if rename_ligand == "y" or rename_ligand == "Y":
        os.system("python3 " + path + "rename_pdb.py " + ligand_file)
    elif rename_ligand == "n" or rename_ligand == "N":
        os.system("cp " + ligand_file + " " + file_base_name + "_renamed.pdb")
    else:
        print ("\n\nEnter Y or N\n\n")
        renaming_ligand()
        


def generate_amber_parameters(): ###Generates amber topology and also AM-BCC charges
    amber_charge = input("Generate amber charges (y/n):  ")
    if amber_charge == "y" or amber_charge == "Y":
        charge = input("Charge of the molecule :  ")
        os.system("antechamber -fi " + file_type + " -fo prepi -i " + file_base_name + "_renamed" + file_type + " -o ligand.prepi -rn " + ligand_name + " -c bcc -pf y -nc " + charge)
    elif amber_charge == "n" or amber_charge == "N":
        os.system("antechamber -fi " + file_type + " -fo prepi -i " + file_base_name + "_renamed" + file_type + " -o ligand.prepi")
    else:
        print ("\n\nEnter Y or N\n\n")
        generate_amber_parameters()
    
    os.system("parmchk2 -f prepi -i ligand.prepi -o ligand.frcmod")
    
    output_tleap = open("tleap.in","w")
    output_tleap.write("source oldff/leaprc.ff99SB\n\
                        source leaprc.gaff\n \
                        loadamberprep ligand.prepi\n\
                        loadamberparams ligand.frcmod\n\
                        ER = loadpdb " + file_base_name + "_renamed.pdb\n\
                        saveAmberParm ER ligand.prmtop ligand.inpcrd\n\
                        quit\n")
    output_tleap.close()

    os.system("tleap -f tleap.in")
        
def post_changes(): ###Converts amber-topology to gromacs-topology
    
    # convert AMBER topology to GROMACS, CHARMM formats
    amber = pmd.load_file('ligand.prmtop', 'ligand.inpcrd')
    # Save a GROMACS topology and GRO file
    try:
        open_top = open("gromacs.top","r")
        open_top.close()
        os.system("mv gromacs.top gromacs_old.top")
        amber.save('gromacs.top')
    except:
        amber.save('gromacs.top')
        
    try:
        open_top = open("gromacs.gro","r")
        open_top.close()
        os.system("mv gromacs.gro gromacs_old.gro")
        amber.save('gromacs.gro')
    except:
        amber.save('gromacs.gro')
    

    #os.system("python3 " + path + "parmed_run.py")

    os.system("chimera " + path + "chimera_conect_entry.py --nogui")


    
def library_entry(): ###For gromacs library entry
    
    os.system("mkdir topology")
    
    try:
        os.system("python3 " + path + "atom_types.py gromacs.top chimera_out.pdb " + ligand_name )   ###REFINED
    except:
        print ("Error running atom_types.py\n\n\n RUN using \n\n\n python3 atom_types.py gromacs.top chimera_out.pdb " + ligand_name )
        
    try:
        os.system("python3 " + path + "rtp_entry.py gromacs.top " + ligand_name + " > topology/rtp_entry.txt")                         ###REFINED
    except:
        print ("Error running rtp_entry.py\n\n\n RUN using \n\n\n python3 rtp_entry.py gromacs.top " + ligand_name )
        
    try:
        os.system("python3 " + path + "dihedrals.py gromacs.top " + ligand_name + " > topology/bonded_entry.txt")                         ###REFINED
    except:
        print ("Error running bonded.py\n\n\n RUN using \n\n\n python3 dihedrals.py gromacs.top " + ligand_name )
        
    try:
        os.system("python3 " + path + "hdb_entry.py chimera_out.pdb " + ligand_name + " > topology/hdb_entry.txt")                           ###REFINED
    except:
        print ("Error running hdb_entry.py\n\n\n RUN using \n\n\n python3 hdb_entry.py chimera_out.pdb " + ligand_name )
        
    try:
        os.system("python3 " + path + "other_entries.py gromacs.top")                                                                      ###REFINED
    except:
        print ("Error running other_entries.py\n\n\n RUN using \n\n\n python3 other_entries.py gromacs.top")
        

    #os.system("rm ATOM_TYPES.txt")



if topology_file == "NEGATIVE":
    if ligand_file[-4:] == ".pdb":
        renaming_ligand()
    elif ligand_file[-4:] == "mol2":
        os.system("cp " + ligand_file + " " + file_base_name + "_renamed" + file_type)
        os.system("obabel -i " + file_type[1:] + " " + file_base_name + "_renamed" + file_type + " -o pdb -O " + file_base_name + "_renamed.pdb")
        
        
    generate_amber_parameters()
    post_changes()
    gromacs_library_entry = input("\n\n\nGromacs library entry output (y/n):\n\n\n")
    if gromacs_library_entry == "Y" or gromacs_library_entry == "y":
        library_entry()
    else:
        None
else:
    if ligand_file != "chimera_out.pdb":
        os.system("cp " + ligand_file + " chimera_out.pdb")
    if topology_file != "gromacs.top":
        os.system("cp " + topology_file + " gromacs.top")
    gromacs_library_entry = input("\n\n\nGromacs library entry output (y/n):\n\n\n")
    if gromacs_library_entry == "Y" or gromacs_library_entry == "y":
        library_entry()
    else:
        None
