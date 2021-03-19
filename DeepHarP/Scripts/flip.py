import vtk
import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description = "A script for flip")
#Add arguments to parser
parser.add_argument("input1",  help="input a ROI")
parser.add_argument("input2",  help="input a mask")
parser.add_argument("output1",  help="output flipped")
parser.add_argument("output2",  help="output flipped")
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

####
if (not os.path.exists(args.input2)):
	print "ERROR: " + args.input2 + " does not exist!"
	sys.exit()

# Read the image data from a NIFTI file
reader2 = vtk.vtkImageReader()
ext = os.path.splitext(args.input2)[1]
if (ext == ".nii" or ext == ".nifti"):
		reader2 = vtk.vtkNIFTIImageReader()
		reader2.SetFileName(args.input2)
else:
		print "ERROR: image format not recognized for " + args.input2
		sys.exit()
reader2.Update()

flipY1 = vtk.vtkImageFlip()
flipY1.SetInputConnection(reader1.GetOutputPort())
flipY1.SetFilteredAxis(2)
flipY1.FlipAboutOriginOff()

flipY2 = vtk.vtkImageFlip()
flipY2.SetInputConnection(reader2.GetOutputPort())
flipY2.SetFilteredAxis(2)
flipY2.FlipAboutOriginOff()

writer1=vtk.vtkNIFTIImageWriter()
writer1.SetInputConnection(flipY1.GetOutputPort())
writer1.SetFileName(args.output1)
writer1.Write()
writer2=vtk.vtkNIFTIImageWriter()
writer2.SetInputConnection(flipY2.GetOutputPort())
writer2.SetFileName(args.output2)
writer2.Write()
