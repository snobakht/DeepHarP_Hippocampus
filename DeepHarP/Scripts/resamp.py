import vtk

import os
import argparse
import sys


parser=argparse.ArgumentParser(description="A script for resampling data")

parser.add_argument("input1", help="edewd")
parser.add_argument("output1", help="deweq")

args=parser.parse_args()
args = parser.parse_args()
if (not os.path.exists(args.input1)):
	print "ERROR: " + args.input1 + " does not exist!"
	sys.exit()

# Read the image data from a NIFTI file
reader1 = vtk.vtkImageReader()
ext = os.path.splitext(args.input1)[1]
if (ext == ".nii" or ext == ".nifti"):
		reader1 = vtk.vtkNIFTIImageReader()
		reader1.SetFileName(args.input1)
else:
		print "ERROR: image format not recognized for " + args.input1
		sys.exit()
reader1.Update()

reslice=vtk.vtkImageReslice()
reslice.SetInputConnection(reader1.GetOutputPort())
reslice.SetOutputSpacing(1,1,1)
reslice.Update()

writer1=vtk.vtkNIFTIImageWriter()
writer1.SetInputData(reslice.GetOutput())
writer1.SetFileName(args.output1)
writer1.Write()
