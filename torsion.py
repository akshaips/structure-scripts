#!/usr/bin/env python3

import os
import glob
import sys
import numpy as np

# '''''''''''''''''''''''''''''''''''''''''
# 'Extracting coordinates if pdb or pdbqt '
# '''''''''''''''''''''''''''''''''''''''''


def For_pdbqt(pdbqt_split, input_atom, input_number, list_num):
    n = 0
    while n < len(pdbqt_split):
        if pdbqt_split[n] == input_atom \
                and pdbqt_split[n + 3] == input_number:  # If chain id present
            if list_num == 1:
                list1.append(pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " " +
                             pdbqt_split[n + 6] + " ")
            if list_num == 2:
                list2.append(pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " " +
                             pdbqt_split[n + 6] + " ")
            if list_num == 3:
                list3.append(pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " " +
                             pdbqt_split[n + 6] + " ")
            if list_num == 4:
                list4.append(pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " " +
                             pdbqt_split[n + 6] + " ")

        if pdbqt_split[n] == input_atom \
                and pdbqt_split[n + 2] == input_number:  # chain id not presnt
            if list_num == 1:
                list1.append(pdbqt_split[n + 3] + " " +
                             pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " ")
            if list_num == 2:
                list2.append(pdbqt_split[n + 3] + " " +
                             pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " ")
            if list_num == 3:
                list3.append(pdbqt_split[n + 3] + " " +
                             pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " ")
            if list_num == 4:
                list4.append(pdbqt_split[n + 3] + " " +
                             pdbqt_split[n + 4] + " " +
                             pdbqt_split[n + 5] + " ")
        n += 1

# '''''''''''''''''''''''''''''''
# 'Extracting coordinates if dlg'
# '''''''''''''''''''''''''''''''


def For_dlg(dlg_split, input_atom, input_number, list_num):
    n = 0
    while n < len(dlg_split):
        splitted = dlg_split[n]
        if splitted[0:6] == "DOCKED":
            split_split = splitted.split()
            if len(input_number) == 1:
                if splitted[17:19] == " " + input_number \
                        and split_split[3] == input_atom:
                    if list_num == 1:
                        list1.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 2:
                        list2.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 3:
                        list3.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 4:
                        list4.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
            if len(input_number) == 2:
                if splitted[17:19] == input_number \
                        and split_split[3] == input_atom:
                    if list_num == 1:
                        list1.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 2:
                        list2.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 3:
                        list3.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 4:
                        list4.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
            if len(input_number) == 3:
                if splitted[16:19] == input_number \
                        and split_split[3] == input_atom:
                    if list_num == 1:
                        list1.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 2:
                        list2.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 3:
                        list3.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")
                    if list_num == 4:
                        list4.append(splitted[39:47] + " " +
                                     splitted[47:55] + " " +
                                     splitted[55:63] + " ")

        n += 1

# '''''''''''''''''''''''''''''''
# 'Extracting coordinates if gro'
# '''''''''''''''''''''''''''''''


def For_gro(gro_split, input_atom, input_number, list_num):
    n = 0
    while n < len(gro_split):
        if gro_split[n] == input_atom:
            if gro_split[n-1][:-3] == input_number:
                if list_num == 1:
                    list1.append(str(float(gro_split[n + 2]) * 10) + " " +
                                 str(float(gro_split[n + 3]) * 10) + " " +
                                 str(float(gro_split[n + 4]) * 10) + " ")
                if list_num == 2:
                    list2.append(str(float(gro_split[n + 2]) * 10) + " " +
                                 str(float(gro_split[n + 3]) * 10) + " " +
                                 str(float(gro_split[n + 4]) * 10) + " ")
                if list_num == 3:
                    list3.append(str(float(gro_split[n + 2]) * 10) + " " +
                                 str(float(gro_split[n + 3]) * 10) + " " +
                                 str(float(gro_split[n + 4]) * 10) + " ")
                if list_num == 4:
                    list4.append(str(float(gro_split[n + 2]) * 10) + " " +
                                 str(float(gro_split[n + 3]) * 10) + " " +
                                 str(float(gro_split[n + 4]) * 10) + " ")

        n += 1

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'Opening the files and sending to respective function to extract coordinates'
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def File_read():
    if input_file1[-6:] == ".pdbqt" or input_file1[-4:] == ".pdb":
        first = For_pdbqt(pdbqt_split1, input_atom1, input_number1, 1)
    elif input_file1[-4:] == ".dlg":
        first = For_dlg(dlg_split1, input_atom1, input_number1, 1)
    else:
        first = For_gro(gro_split1, input_atom1, input_number1, 1)

    if input_file2[-6:] == ".pdbqt" or input_file2[-4:] == ".pdb":
        second = For_pdbqt(pdbqt_split2, input_atom2, input_number2, 2)
    elif input_file2[-4:] == ".dlg":
        second = For_dlg(dlg_split2, input_atom2, input_number2, 2)
    else:
        second = For_gro(gro_split2, input_atom2, input_number2, 2)

    if input_file3[-6:] == ".pdbqt" or input_file3[-4:] == ".pdb":
        third = For_pdbqt(pdbqt_split3, input_atom3, input_number3, 3)
    elif input_file3[-4:] == ".dlg":
        third = For_dlg(dlg_split3, input_atom3, input_number3, 3)
    else:
        third = For_gro(gro_split3, input_atom3, input_number3, 3)

    if input_file4[-6:] == ".pdbqt" or input_file4[-4:] == ".pdb":
        fourth = For_pdbqt(pdbqt_split4, input_atom4, input_number4, 4)
    elif input_file4[-4:] == ".dlg":
        fourth = For_dlg(dlg_split4, input_atom4, input_number4, 4)
    else:
        fourth = For_gro(gro_split4, input_atom4, input_number4, 4)
    List_making()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'Making equal size list of coordinates to find all the angles'
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def List_making():
    list_len = [len(list1), len(list2), len(list3), len(list4)]
    angle_num = sorted(list_len)
    list1_string = ""
    list2_string = ""
    list3_string = ""
    list4_string = ""

    if len(list1) != angle_num[-1]:
        n = 1
        while n < angle_num[-1]:
            list1.append(list1[0])
            n += 1
    if len(list2) != angle_num[-1]:
        n = 1
        while n < angle_num[-1]:
            list2.append(list2[0])
            n += 1
    if len(list3) != angle_num[-1]:
        n = 1
        while n < angle_num[-1]:
            list3.append(list3[0])
            n += 1
    if len(list4) != angle_num[-1]:
        n = 1
        while n < angle_num[-1]:
            list4.append(list4[0])
            n += 1

    for each1 in list1:
        list1_string += each1
    for each2 in list2:
        list2_string += each2
    for each3 in list3:
        list3_string += each3
    for each4 in list4:
        list4_string += each4

    Angle_find(list1_string, list2_string, list3_string, list4_string)

# '''''''''''''''''''''''''''''''''''''''''''''''''
# ' Finding angles and output is written to a file'
# '''''''''''''''''''''''''''''''''''''''''''''''''


def Angle_find(list1_string, list2_string, list3_string, list4_string):
    list1_split = list1_string.split()
    list2_split = list2_string.split()
    list3_split = list3_string.split()
    list4_split = list4_string.split()
    n = 0
    m = 0
    output = open(output_filename, "a")
    print("\n" + output_filename + "\n")
    while n < len(list1):
        a = np.array([float(list1_split[m]),
                      float(list1_split[m + 1]),
                      float(list1_split[m + 2])])
        b = np.array([float(list2_split[m]),
                      float(list2_split[m + 1]),
                      float(list2_split[m + 2])])
        c = np.array([float(list3_split[m]),
                      float(list3_split[m + 1]),
                      float(list3_split[m + 2])])
        d = np.array([float(list4_split[m]),
                      float(list4_split[m + 1]),
                      float(list4_split[m + 2])])
        v1 = -1.0*(b - a)
        v2 = c - b
        v3 = d - c
        cp = np.cross(v1, v2)
        cp2 = np.cross(v3, v2)
        cp3 = np.cross(cp, cp2)
        y = np.dot(cp3, v2) * (1.0 / np.linalg.norm(v2))
        x = np.dot(cp, cp2)
        angle = np.arctan2(y, x)
        n += 1
        m += 3
        output.write(str(np.degrees(angle)) + "\n")
        print((np.degrees(angle)))

# ''''''''''''''''''
# ' all inputs     '
# ''''''''''''''''''


if len(sys.argv) <= 13:
    print("\n \nUSAGE = python torsion.py filename atom_type1 atom_number1\
filename atom_type2 atom_number2 filename atom_type3 atom_number3\
filename atom_type4 atom_number4 output_filename \n\n or \n\npython\
torsion.py test.pdb CA 156 test.gro CB 130 test.dlg C 8 test.pdb CA\
100 test_torsion.txt \n \n \nUse pdb/gro/dlg/pdbqt")
else:
    input_file1 = sys.argv[1]
    input_atom1 = sys.argv[2]
    input_number1 = sys.argv[3]
    input_file2 = sys.argv[4]
    input_atom2 = sys.argv[5]
    input_number2 = sys.argv[6]
    input_file3 = sys.argv[7]
    input_atom3 = sys.argv[8]
    input_number3 = sys.argv[9]
    input_file4 = sys.argv[10]
    input_atom4 = sys.argv[11]
    input_number4 = sys.argv[12]
    output_filename = sys.argv[13]

    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # ' check inputs are pdb,pdbqt or dlg and assigning filename to variables'
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    if input_file1[-6:] == ".pdbqt" or input_file1[-4:] == ".pdb":
        pdbqt_open = open(input_file1, "r").read()
        pdbqt_split1 = pdbqt_open.split()
    elif input_file1[-4:] == ".dlg":
        dlg_open = open(input_file1, "r")
        dlg_split1 = dlg_open.readlines()
    elif input_file1[-4:] == ".gro":
        gro_open = open(input_file1, "r").read()
        gro_split1 = gro_open.split()

    if input_file2[-6:] == ".pdbqt" or input_file2[-4:] == ".pdb":
        pdbqt_open = open(input_file2, "r").read()
        pdbqt_split2 = pdbqt_open.split()
    elif input_file2[-4:] == ".dlg":
        dlg_open = open(input_file2, "r")
        dlg_split2 = dlg_open.readlines()
    elif input_file2[-4:] == ".gro":
        gro_open = open(input_file2, "r").read()
        gro_split2 = gro_open.split()

    if input_file3[-6:] == ".pdbqt" or input_file3[-4:] == ".pdb":
        pdbqt_open = open(input_file3, "r").read()
        pdbqt_split3 = pdbqt_open.split()
    elif input_file3[-4:] == ".dlg":
        dlg_open = open(input_file3, "r")
        dlg_split3 = dlg_open.readlines()
    elif input_file3[-4:] == ".gro":
        gro_open = open(input_file3, "r").read()
        gro_split3 = gro_open.split()

    if input_file4[-6:] == ".pdbqt" or input_file4[-4:] == ".pdb":
        pdbqt_open = open(input_file4, "r").read()
        pdbqt_split4 = pdbqt_open.split()
    elif input_file4[-4:] == ".dlg":
        dlg_open = open(input_file4, "r")
        dlg_split4 = dlg_open.readlines()
    elif input_file4[-4:] == ".gro":
        gro_open = open(input_file4, "r").read()
        gro_split4 = gro_open.split()

    # ''''''''''''''''''''''''''''''''''''''
    # 'Global list for to store coordinates'
    # ''''''''''''''''''''''''''''''''''''''

    list1 = []
    list2 = []
    list3 = []
    list4 = []

    File_read()
