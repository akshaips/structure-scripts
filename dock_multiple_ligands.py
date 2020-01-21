#!/usr/bin/env python3

import os
import sys
import glob
from threading import Thread
from multiprocessing import Pool
import multiprocessing


def usage():
    print ("\n\nUSAGE: \n\n\tpython dock_multiple_ligands.py protein.pdbqt dpf_file.dpf\n\n")

pdbqts = glob.glob("*.pdbqt")
protein_file = sys.argv[1]
dpf_file = sys.argv[2]

open_dpf = open(dpf_file,"r").readlines()

def processing(data):
    if data != protein_file:
        save_dpf = open(data[:-6] + ".dpf","w")
        output = ""
        for entry in open_dpf:
            if "move" not in entry:
                output += entry
            else:
                output += "move " + data + " # small molecule\n"
        save_dpf.write(output)
        save_dpf.close()
        os.system("autodock4 -p " + data[:-6] + ".dpf -l " + data[:-6] + ".dlg")

        
def do_dock(data_set):
    if __name__ == '__main__':
        p = Pool(num_threads)
        p.map(processing, data_set)
        
if len(sys.argv) <= 2:
    usage()
else:
    num_threads = int(input("Number of threads to be used ('0' to use all the threads) : "))
    if num_threads == 0:
        num_threads = multiprocessing.cpu_count()  # change this to number of threads the program should run in
    do_dock(pdbqts)
