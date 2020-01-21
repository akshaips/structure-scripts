Usage:

python3 library_entry.py ligand_file.pdb/mol2 ligand_resname (topology optional)

if topology is given, library entry parameters are taken from the given topology



Scripts:


library_entry.py --> 
Takes arguments and call all the scripts in order with the necessary arguments for the scripts
Generates AM-BCC charges and amber topology
Converts amber topolgy to gromacs topology

atom_types.py --> 
Makes a text file "ATOMTYPES.txt" containing ligand's atomname atomtype and atomnumber
This is created for easy reference for the rest of the scripts


chimera_conect_entry.py -->
Opens ligand gro file output from the script which converts amber to gromacs and convert the gro to pdb with the conect entries for the hdb (hydrogen bond) entry


bonded.py -->
Takes bonds,angles,dihedrals and improper values from the topology and converts it into a format (as mentioned in the ppt) to enter in to gromacs library


other_entries.py-->
Makes gromacs library compatible entries for .atp and non-bonded entries


rtp_entry.py -->
Makes gromacs library compatible entries for aminoacids.rtp


rename_pdb.py --> 
Takes input argument for renaming the ligand as mentioned in the ppt
rename_pdb_supp.py contains functions for the renaming of both heavy atoms and hydrogens
Renaming is done using CONECT entries, hence proper CONECT is mandatory


hdb_entry.py -->
Takes input argument for .hdb entry as mentioned in the ppt
hdb_entry_supp.py contains functions for the same
CONECT entries are mandatory for the entry
(Hydrogen types are written as "#" in the output, which has to be written by the user using gromacs manual)


***The arguments for the individual scripts are written in the library_entry.py
