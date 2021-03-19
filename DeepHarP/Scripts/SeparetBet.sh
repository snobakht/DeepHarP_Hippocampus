#!/bin/bash


root_dir=$"/home/snobakht/Desktop"



cd  $root_dir/DeepHarp/Brains/

gunzip *.nii.gz

for i in `ls *_Bet.nii`;do

name=${i%_Bet.nii}


bet $i  ${name}_Bet.nii -f 0.3 -B
done
