# Structure Scripts

## Analysis scripts
distance.py --> To find distance between two atoms (from one to two different files)

angle.py --> To find angle between three atoms (from one to three different files)

torsion.py --> To find dihedral angle between four atoms (from one to four different files)

Contact_score_analysis_old.py --> Find contact score (need supporting scripts for proper function)

## Molecular dynamics files
parameterize.py --> Paramaterize a molecule for molecular dynamics simulation. (Output is Gromacs compatible topology file)

## Autodock files
dock_multiple_ligands.py --> Dock multiple ligands to a single protein

make_gpf_dpf.py --> Make gpf and dpf files for docking (Multiple protein gpf and dpf for to dock with single ligand molecule)
grid_dock_mp.py --> Make map files from gpf and docked files from dpf

dlg_to_pdb_V2.py --> To convert dlg(output of autodock) to pdb format. (Autodock support files)
