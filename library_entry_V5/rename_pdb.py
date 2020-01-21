import rename_pdb_supp as rs
import sys
import os

filename = sys.argv[1]

def heavy_atom_check():
	rename_heavy_atoms = input("Rename heavy atoms (Y/N):")
	if rename_heavy_atoms == "Y" or rename_heavy_atoms == "y":
		rs.pdb.rename_heavy_atoms(filename)
	elif rename_heavy_atoms == "N" or rename_heavy_atoms == "n":
		os.system("cp " + filename + " " + filename[:-4] + "_heavy_atoms_renamed.pdb")
	else:
		print ("\n\nEnter Y or N\n\n")
		heavy_atom_check()



def hydrogen_check():
	rename_hydrogen = input("Rename hydrogens (Y/N):")
	if rename_hydrogen == "Y" or rename_hydrogen == "y":
		rs.pdb.write_renamed(filename[:-4] + "_heavy_atoms_renamed.pdb",(rs.pdb.conect(filename[:-4] + "_heavy_atoms_renamed.pdb")))
	elif rename_hydrogen == "N" or rename_hydrogen == "n":
		os.system("cp " + filename[:-4] + "_heavy_atoms_renamed.pdb " + filename[:-4] + "_renamed.pdb")
	else:
		print ("\n\nEnter Y or N\n\n")
		hydrogen_check()


heavy_atom_check()
hydrogen_check()


os.system("rm " + filename[:-4] + "_heavy_atoms_renamed.pdb")