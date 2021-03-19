import os
import sklearn 
import glob
import random
import math
import argparse

parser = argparse.ArgumentParser(
    description = "A script that segments hipocampus")
#Add arguments to parser
parser.add_argument("input1", type=str, help="Input path of data")
parser.add_argument("input2", type=str, help="Input filename")
parser.add_argument("input3", type=str, help="Input substring")

args = parser.parse_args()


def Predwriter(path,filename,substring):
 items = os.listdir(path)
 for names in items:
  if names.endswith(substring):
   
  
   with open (filename, "a") as f:
   
     f.write("%s\n" %names)

###Epilepsy

Predwriter(args.input1 , args.input2, args.input3)
