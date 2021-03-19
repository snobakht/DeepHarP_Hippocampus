
DeepHarp is a tool that uses atlas based segmentation and Convolutional Neural Network to segment hippocampus from T1 MRI images.
The fully-connected DeepMedic CNN architecture, originally designed for brain lesion segmentation and  described in detail in
Kamnitsas K, Ledig C, Newcombe VFJ, et al. Efficient multi-scale 3D CNN with fully connected CRF for accurate brain lesion segmentation. Med Image Anal. 2017;36:61-78. doi:10.1016/j.media.2016.10.004
was optimized for hippocampus segmentation in this work. The DeepMedic framework is open source and publicly available on https://github.com/deepmedic/deepmedic. 

In order to use the tool take these steps:

1- Download and install DeepMedic    ----> https://github.com/deepmedic/deepmedic

2- Download and install NiftyReg  ---->  http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg_install

3-Download DeepHarp  

4- Download and install vtk ---> https://anaconda.org/anaconda/vtk

5- Place all the brain extracted T1 images in the folder Brains within DeepHarp folder.Make sure the extenstion is _Bet.nii

6- Replace the root directory in main.sh within DeepHarp/Scripts folder

7- Run source main.sh to start registrations and segmentations. Results will appear in folder DeepHarp/predictions/testSessionTiny/predictions

8- The cropped ROI will be within folder DeepHarp/Brains

