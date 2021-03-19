
DeepHarp is a tool that uses atlas based segmentation and Convolutional Neural Network to segment hippocampus from T1 MRI images.

In order to use the tool take these steps:

1- Download and install DeepMedic    ----> https://github.com/deepmedic/deepmedic

2- Download and install NiftyReg  ---->  http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg_install

3-Download DeepHarp  

4- Download and install vtk ---> https://anaconda.org/anaconda/vtk

5- Place all the brain extracted T1 images in the folder Brains within DeepHarp folder.Make sure the extenstion is _Bet.nii

6- Replace the root directory in main.sh within DeepHarp/Scripts folder

7- Run source main.sh to start registrations and segmentations. Results will appear in folder DeepHarp/predictions/testSessionTiny/predictions

8- The cropped ROI will be within folder DeepHarp/Brains

