import vtk 

reader=vtk.vtkNIFTIImageReader()

reader.SetFileName("pt101_T1_o_brain.nii")
reader.Update()
image=reader.GetOutput()

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
Array=TightBounder(image)
print("Image resizing in progress!")
#crop image using above bounding box
HipoCrop=ImageCropper(image,Array[0],Array[1],Array[2],Array[3],Array[4],Array[5])
print("croppedimage..............")
print(HipoCrop.GetExtent())
print("origImage.................")
print(image.GetExtent())
pad = vtk.vtkImageConstantPad()
pad.SetInputData(HipoCrop)
pad.SetOutputWholeExtent(-Array[0],image.GetExtent()[1]-Array[0],-Array[2],image.GetExtent()[3]-Array[2],-Array[4],image.GetExtent()[5]-Array[4])



pad.SetConstant(0)
pad.Update()
writer6=vtk.vtkNIFTIImageWriter()
writer6.SetInputConnection(pad.GetOutputPort())
writer6.SetFileName("SegmentedNoPostProcess_Hipo.nii")
writer6.Write()

reader1=vtk.vtkNIFTIImageReader()

reader1.SetFileName("SegmentedNoPostProcess_Hipo.nii")
reader1.Update()
image1=reader.GetOutput()
print("finalImage.................")
print(reader1.GetOutput().GetExtent())

reslice = vtk.vtkImageReslice()
reslice.SetInputConnection(reader1.GetOutputPort())
#reslice.SetInformationInput(reader.GetOutput())
reslice.SetOutputExtent(-image1.GetExtent()[1],0,-image1.GetExtent()[3],0,-image1.GetExtent()[5],0)
reslice.Update()
writer61=vtk.vtkNIFTIImageWriter()
writer61.SetInputConnection(reslice.GetOutputPort())
writer61.SetFileName("reslice_Hipo.nii")
writer61.Write()

