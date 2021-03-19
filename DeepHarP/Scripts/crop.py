from __future__ import division
import vtk

import math
import random
import argparse
import os
import sys
#Create argument parser
parser = argparse.ArgumentParser(
    description = "A script that segments hipocampus")
#Add arguments to parser
parser.add_argument("input1",  help="Input should be a Nifti image which is  dilated mask including hipocampus")
parser.add_argument("input2",  help="Input should be a Nifti image of patient's region of interest")
#parser.add_argument("input3",  help="Input should be a Nifti image of patient's ground truth")
#parser.add_argument("-arg1","--NumClus", type="int", help="Number of initial clusters")
#Outputs


#parser.add_argument("input3",  help="Input should be a Nifti image of patient's brain substructure Manually Segmented")

parser.add_argument("output1",  help="output is cropped mask")
parser.add_argument("output2",  help="output is cropped ROI")
#parser.add_argument("output3",  help="output is cropped GT")
#parser.add_argument("output2",  help="Input should be a Nifti image of patient's brain substructure Manually Segmented")
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
im1=reader1.GetOutput()
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
im2=reader2.GetOutput()
'''
if (not os.path.exists(args.input3)):
	print "ERROR: " + args.input3 + " does not exist!"
	sys.exit()

# Read the image data from a NIFTI file
reader3 = vtk.vtkImageReader()
ext = os.path.splitext(args.input3)[1]
if (ext == ".nii" or ext == ".nifti"):
		reader3 = vtk.vtkNIFTIImageReader()
		reader3.SetFileName(args.input3)
else:
		print "ERROR: image format not recognized for " + args.input3
		sys.exit()
reader3.Update()
im3=reader3.GetOutput()

'''
'''Define all the required functions for segmentation'''
print("Defining required functions for segmentation...")
#......................................................
#A function that creates an image with same structure as input image but all voxels are zero
def ZeroImage (image):
    image1=vtk.vtkImageData()
    image1.DeepCopy(image)
    for z   in range(0,  image.GetDimensions()[2]):
     for y   in range(0,  image.GetDimensions()[1]):
       for x  in range (0,  image.GetDimensions()[0]):
        image1.SetScalarComponentFromFloat(x,y,z,0,0)
    return(image1)

def ImageCropper(Image,X1, X2,Y1,Y2, Z1,Z2):
     CroppedImage = vtk.vtkExtractVOI()
     CroppedImage.SetInputData(Image)
     CroppedImage.SetVOI(X1, X2,Y1,Y2, Z1,Z2)
     CroppedImage.Update()
     writer=vtk.vtkNIFTIImageWriter()
     writer.SetInputConnection(CroppedImage.GetOutputPort())
     writer.SetFileName("CroppedImageout.nii")
     writer.Write()
     reader=vtk.vtkNIFTIImageReader()
     reader.SetFileName("CroppedImageout.nii")
     reader.Update()
     image=reader.GetOutput()
     return(image)
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#A function that finds extent for drawing a tight bounding box around a binary mask
def TightBounder(image):
   yvector=[]
   zvector=[]
   xvector=[]
   for z   in range(0,  image.GetDimensions()[2]):
     for y   in range(0,  image.GetDimensions()[1]):
       for x  in range (0,  image.GetDimensions()[0]):
         vox=image.GetScalarComponentAsFloat(x,y,z,0)
         if vox==1:
           yvector.append(y)
           zvector.append(z)
           xvector.append(x)

   xmin=min(xvector)
  
   xmax=max(xvector)
   
   zmin=min(zvector)
   
   zmax=max(zvector)
   
   ymin=min(yvector)
  
   ymax=max(yvector)
   
   Array=[xmin,xmax,ymin,ymax,zmin,zmax]
   return(Array)

Array=TightBounder(im1)

X1=Array[0]
X2=Array[1]
Y1=Array[2]
Y2=Array[3]
Z1=Array[4]
Z2=Array[5]

im1crop=ImageCropper(im1,X1,X2,Y1,Y2,Z1,Z2)
im2crop=ImageCropper(im2,X1,X2,Y1,Y2,Z1,Z2)
#im3crop=ImageCropper(im3,X1,X2,Y1,Y2,Z1,Z2)


writer1=vtk.vtkNIFTIImageWriter()
writer1.SetInputData(im1crop)
writer1.SetFileName(args.output1)
writer1.Write()

writer2=vtk.vtkNIFTIImageWriter()
writer2.SetInputData(im2crop)
writer2.SetFileName(args.output2)
writer2.Write()

