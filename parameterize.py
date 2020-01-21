import os
import sys
import parmed as pmd

if len(sys.argv) < 2:
    print ("Usage python3 parameterize.py ligand.pdb UNL")
    exit()

print("Make sure CONECT entries are present in the ligand")
ligand_file = sys.argv[1]
ligand_name = sys.argv[2]
ffield = input("1: AMBER:ff14SB \n\
2: AMBER:ff99SB \n\
3: AMBER:ff99SB-IDLN \n\
4: AMBER:ff03 \n\
5: AMBER:ff99 \n\
6: AMBER:ff96 \n\
7: AMBER:ff03\n\n\
Enter force field:   ")

amber_charge = input("Generate amber charges (y/n):  ")
if amber_charge == "y" or amber_charge == "Y":
    charge = input("Charge of the molecule:   ")
    os.system("antechamber -fi pdb -fo prepi -i " + ligand_file +
              " -o " + ligand_name + ".prepi -rn " + ligand_name + " -c bcc -pf y -nc " +
              charge)
elif amber_charge == "n" or amber_charge == "N":
    os.system("antechamber -fi pdb -fo prepi -i " + ligand_file + " -o " + ligand_name + ".prepi")
else:
    print("Enter Y or N")
    exit()

os.system("parmchk2 -f prepi -i " + ligand_name + ".prepi -o " + ligand_name + ".frcmod")

if ffield == "1":
    ff = "ff14SB"
elif ffield == "2":
    ff = "ff99SB"
elif ffield == "3":
    ff = "ff99SBildn"
elif ffield == "4":
    ff = "ff03"
elif ffield == "5":
    ff = "ff99"
elif ffield == "6":
    ff = "ff96"
elif ffield == "7":
    ff = "ff03"
else:
    print("Enter 1 to 7")

output_tleap = open("tleap.in", "w")
output_tleap.write("source oldff/leaprc." + ff + "\n\
source leaprc.gaff\n \
loadamberprep " + ligand_name + ".prepi\n\
loadamberparams " + ligand_name + ".frcmod\n\
ER = loadpdb " + ligand_file + "\n\
saveAmberParm ER " + ligand_name + ".prmtop " + ligand_name + ".inpcrd\n\
quit\n")
output_tleap.close()

os.system("tleap -f tleap.in")

try:
    os.remove("gromacs.top")
except:
    None

try:
    os.remove("gromacs.gro")
except:
    None


def Convert_topology():
    # convert AMBER topology to GROMACS, CHARMM formats
    amber = pmd.load_file(ligand_name + '.prmtop',  ligand_name + '.inpcrd')
    # Save a GROMACS topology and GRO file
    amber.save(ligand_name + '.top')
    amber.save(ligand_name + '.gro')

Convert_topology()
