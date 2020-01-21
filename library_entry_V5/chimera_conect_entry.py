from chimera import runCommand as rc
from chimera import replyobj
#import sys

#filename = sys.argv[1]
#outfile = sys.argv[2]

rc("open gromacs.gro")
rc("write format pdb 0 chimera_out.pdb")
rc("close all")
rc("stop now")
rc("quit")
