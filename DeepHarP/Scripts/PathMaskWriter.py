import os
import sklearn 
import glob
import random
import math
import argparse



parser = argparse.ArgumentParser(
    description = "A script that segments hipocampus")
#Add arguments to parser
parser.add_argument("input1", type=str, help="Input path ROI.txt")
parser.add_argument("input2", type=str, help="Input path of Mask.txt")

args = parser.parse_args()


with open(args.input1, "rt") as fin:
    with open(args.input2, "wt") as fout:
        for line in fin:
            fout.write(line.replace('_ROIFine', '_MaskFine'))


