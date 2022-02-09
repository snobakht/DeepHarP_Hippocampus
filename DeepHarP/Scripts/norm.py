from __future__ import division
import vtk
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk
import math
import random
import argparse
import os
import sys
import scipy.optimize as optimize
import collections


#Create argument parser
parser = argparse.ArgumentParser(
    description = "A script that enhances contrast")
#Add arguments to parser
parser.add_argument("input1",  help="Input should be a Nifti ROI image")
parser.add_argument("output",  help="output is zeromean unaryvariance roi image")

#Parse arguments
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
ROI=reader1.GetOutput()

numpyArray=vtk_to_numpy(ROI.GetPointData().GetScalars())
sd=np.std(numpyArray)
mn=np.mean(numpyArray)
ROICopy=vtk.vtkImageData()
ROICopy.DeepCopy(ROI)

for z   in range(0,  ROI.GetDimensions()[2]):
     for y   in range(0,  ROI.GetDimensions()[1]):
       for x  in range (0,  ROI.GetDimensions()[0]):
        vox= ROI.GetScalarComponentAsFloat(x,y,z,0)
        newvox=(vox-mn)/sd
        ROICopy.SetScalarComponentFromFloat(x,y,z,0,newvox)
        
writer=vtk.vtkNIFTIImageWriter()
writer.SetInputData(ROICopy)
writer.SetFileName(args.output)
writer.Write()

