#!/usr/bin/env python3

import os
import sys
import glob
from threading import Thread
from multiprocessing import Pool
import multiprocessing


#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#" Does multiple docking and making map files, Run grid first and run the program "
#" again using DOCK as the option for docking,                                    "
#" Change num_threads = 'number' to allocate the processors to be used            "
#" Give input option as capital GRID or DOCK for respective action                "
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def usage():
    print ("\n\nUSAGE: \n\n\tpython grid_dock_mp.py GRID \n\n\t\tor\n\n\tpython grid_dock_mp.py DOCK \n\n\t\tor\n\n\tpython grid_dock_mp.py BOTH \n\n")

gpf_s = glob.glob("*.gpf")
dpf_s = glob.glob("*.dpf")

def processing(data):
    if option == "GRID":
        os.system("autogrid4 -p " + data + " -l " + data[:-4] + ".glg")
    if option == "DOCK":
        os.system("autodock4 -p " + data + " -l " + data[:-4] + ".dlg")
	if option == "BOTH":
		os.system("autogrid4 -p " + data + " -l " + data[:-4] + ".glg")
		os.system("autodock4 -p " + data[:-4] + " -l " + data[:-4] + ".dlg")

def paralleling(data_set):
    n = 0
    if __name__ == '__main__':
        p = Pool(num_threads)
        p.map(processing, data_set)
        n += 1
		
if len(sys.argv) <= 1:
	usage()
else:
	option = sys.argv[1]
	num_threads = int(input("Number of threads to be used ('0' to use all the threads) : "))
	if num_threads == 0:
		num_threads = multiprocessing.cpu_count()  # change this to number of threads the program should run in
	if option == "GRID":
		paralleling(gpf_s)
	elif option == "DOCK":
		paralleling(dpf_s)
	elif option == "BOTH":
		paralleling(gpf_s)
	else:
		usage()
