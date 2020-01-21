import os
import sys

#print ("\n\n\nEnter below ones in atomtypes.atp\n\n\n")

filename = sys.argv[1]
open_top = open(filename,"r")
top_lines = open_top.readlines()
open_top.close()
outfile_atp = open("topology/atp_entry.txt","w")
outfile_atp.write("\n\n\nEnter below ones in atomtypes.atp\n\n\n")
outfile_non_bonded = open("topology/non_bonded_entry.txt","w")
outfile_non_bonded.write("\n\n\nEnter below ones in ffnonbonded.itp\n\n\n")
def make_list():
	n = 0
	count = 0
	while n < len(top_lines):
		top_split = top_lines[n].split()
		if len(top_split) > 1:
			if top_split[0][0] != ";":
				if top_split[0] == "[" and top_split[1] == "atomtypes" and top_split[2] == "]":
					initial_n = n
					count += 1
			if len(top_lines)-1  == n:
				final_n = n
				break
			if len(top_split) > 0 and count == 1:
				if initial_n != 0 and n > initial_n and top_split[0] == "[":
					final_n = n
					break
		n += 1
		
	n = initial_n
	while n < final_n:
		top_split = top_lines[n].split()
		if len(top_split) > 1 and top_split[0][0] != ";" and top_split[0] != "[":
			#print (top_split[0] + " " + top_split[2] + " ;")
			outfile_atp.write(top_split[0] + " " + top_split[2] + "\t;\n")
		n += 1
	
	n = initial_n
	while n < final_n:
		top_split = top_lines[n].split()
		if len(top_split) > 1 and top_split[0][0] != ";" and top_split[0] != "[":
			#print (top_split[0] + "\t" + top_split[1] + "\t"  + top_split[2] + "\t"  +top_split[3] + "\t"  +top_split[4] + "\t"  +top_split[5] + "\t"  +top_split[6] + "\t;")
			outfile_non_bonded.write(top_split[0] + "\t" + top_split[1] + "\t"  + top_split[2] + "\t"  +top_split[3] + "\t"  +top_split[4] + "\t"  +top_split[5] + "\t"  +top_split[6] + "\t;\n")
		n += 1
	
make_list()