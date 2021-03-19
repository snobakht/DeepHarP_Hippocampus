#!/bin/bash


 
root_dir=$"/home/snobakht/Desktop"



cd  $root_dir/DeepHarp/Brains/
gunzip *.nii.gz

for i in `ls *_Bet.nii`;do

name=${i%_Bet.nii}
reg_aladin -ref  $root_dir/DeepHarp/Atlases/MNI152_T1_1mm_brain.nii.gz  -flo ${name}_Bet.nii   -rigOnly  -res  ${name}_Aladin.nii



reg_f3d  -ref  ${name}_Aladin.nii -flo  $root_dir/DeepHarp/Atlases/MNI152_T1_1mm_brain.nii.gz   -res ${name}_regf3d_result.nii -cpp ${name}_regf3d_cpp.nii


reg_resample -target  ${name}_Aladin.nii -source  $root_dir/DeepHarp/Atlases/RightHippocampusBinDil.nii.gz -cpp ${name}_regf3d_cpp.nii -NN 0 -res ${name}_Right.nii

reg_resample -target   ${name}_Aladin.nii -source  $root_dir/DeepHarp/Atlases/LeftHippocampusBinDil.nii.gz -cpp ${name}_regf3d_cpp.nii -NN 0 -res ${name}_Left.nii

done

gunzip *.nii.gz
for f in `ls *_Aladin.nii`;do

name=${f%_Aladin.nii*}

python  $root_dir/DeepHarp/Scripts/crop.py ${name}_Right.nii ${name}_Aladin.nii  ${name}_croppedMask_Right.nii ${name}_croppedROI_Right.nii 
python  $root_dir/DeepHarp/Scripts/crop.py ${name}_Left.nii  ${name}_Aladin.nii ${name}_croppedMask_Left.nii ${name}_croppedROI_Left.nii 
python  $root_dir/DeepHarp/Scripts/Resamp.py ${name}_croppedROI_Right.nii  ${name}_ResampRight.nii 
python  $root_dir/DeepHarp/Scripts/Resamp.py ${name}_croppedROI_Left.nii  ${name}_ResampLeft.nii
python  $root_dir/DeepHarp/Scripts/Norm.py ${name}_ResampRight.nii ${name}_NormRight.nii 
python  $root_dir/DeepHarp/Scripts/Norm.py ${name}_ResampLeft.nii  ${name}_NormLeft.nii

python  $root_dir/DeepHarp/Scripts/flip.py ${name}_NormRight.nii ${name}_croppedMask_Right.nii ${name}_ROIFineRight.nii ${name}_MaskFineRight.nii
python  $root_dir/DeepHarp/Scripts/flip.py ${name}_NormLeft.nii ${name}_croppedMask_Left.nii ${name}_ROIFineLeft.nii ${name}_MaskFineLeft.nii


done



python  $root_dir/DeepHarp/Scripts/PathWriter.py "$root_dir/DeepHarp/Brains/" "$root_dir/DeepHarp/Configurations/ROI.txt" "_ROIFineRight.nii"
python  $root_dir/DeepHarp/Scripts/PathWriter.py "$root_dir/DeepHarp/Brains/" "$root_dir/DeepHarp/Configurations/ROI.txt" "_ROIFineLeft.nii"

python  $root_dir/DeepHarp/Scripts/PathMaskWriter.py   "$root_dir/DeepHarp/Configurations/ROI.txt"  "$root_dir/DeepHarp/Configurations/Mask.txt"

python  $root_dir/DeepHarp/Scripts/PredWriter.py "$root_dir/DeepHarp/Brains/" "$root_dir/DeepHarp/Configurations/Predict.txt" "_ROIFineRight.nii"
python  $root_dir/DeepHarp/Scripts/PredWriter.py "$root_dir/DeepHarp/Brains/" "$root_dir/DeepHarp/Configurations/Predict.txt" "_ROIFineLeft.nii"

cd  $root_dir/DeepHarp/deepmedic-master
###if gpu available at below add -dev cuda0




./deepMedicRun -test  "$root_dir/DeepHarp/Configurations/testConfig.cfg" -model  "$root_dir/DeepHarp/Configurations/modelConfig.cfg" 

cd  $root_dir/DeepHarp/Configurations/

rm Predict.txt Mask.txt ROI.txt

cd  $root_dir/DeepHarp/predictions/testSessionTiny/predictions

rm *ProbMapClass*

cd  $root_dir/DeepHarp/Brains/

rm *MaskFine*  *Resamp* *Norm* *Aladin*  *.txt  CroppedImageout.nii  *regf3d*  *croppedROI* *croppedMask* *_Left.nii  *_Right.nii

