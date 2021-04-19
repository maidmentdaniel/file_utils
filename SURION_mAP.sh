#!/bin/bash


data="cfg/yolov4_Surion_OI_2.data"
config="cfg/yolov4_Surion_OI_2.cfg"
weights="/home/ryzen1/Surion/darknet/backup/yolov4_Surion_OI_2_best.weights"
trainingdir="/home/ryzen1/Surion/training/yolov4_Surion_OI_2/mAP"

for wghts in /home/ryzen1/Surion/darknet/backup/*.weights
	do
		for iou in 0.25 0.5 0.75
			do
				echo "#############################################################################################"
				echo "#############################################################################################"
				echo "#############################################################################################"		
				echo "# Calculate mAP" $wghts "iou" $iou | tee -a $wghts.txt
				echo "#############################################################################################"
				echo "#############################################################################################"
				echo "#############################################################################################"
				./darknet detector map $data $config $wghts -iou_thresh $iou | tee -a $wghts.txt
			done
		mv $wghts.txt /home/ryzen1/Surion/darknet/backup/yolov4_Surion_OI_2/
		mv $wghts /home/ryzen1/Surion/darknet/backup/yolov4_Surion_OI_2/
	done
echo "Done"
