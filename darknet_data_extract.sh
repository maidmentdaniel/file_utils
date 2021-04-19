dst=/home/ryzen1/Surion/training/yolov4_Surion_OI_2/extracted_results.txt

for file in /home/ryzen1/Surion/darknet/backup/yolov4_Surion_OI_2/*.weights.txt
	do
		grep -Eao '[0-9]{1,6}.weights iou 0.25$' $file --max-count=100000 -B 0 -A 0 | tee -a $dst
		grep -Eao 'person, ap = [0-9][0-9]\.[0-9]+\%   	 \(TP = [0-9]{0,5}, FP = [0-9]{0,5}\)' $file --max-count=100000 -B 0 -A 0| tee -a $dst
		grep -Eao 'vehicle, ap = [0-9][0-9]\.[0-9]+\%   	 \(TP = [0-9]{0,5}, FP = [0-9]{0,5}\)' $file --max-count=100000 -B 0 -A 0 | tee -a $dst
		# grep -Ea 'conf_thresh' $file --max-count=100000 -B 0 -A 0 | tee -a $dst
		grep -Eao 'conf_thresh = 0.25, TP = [0-9]{1,7}, FP = [0-9]{1,7}, FN = [0-9]{1,7}, average IoU = [0-9]{1,2}\.[0-9]{1,2}' $file --max-count=100000 -B 0 -A 0 | tee -a $dst
		grep -Eao '\(mAP@0\.[0-9]{1,2}\) = 0\.[0-9]{1,7}, or [0-9]{1,2}\.[0-9]{1,2} %' $file --max-count=100000 -B 0 -A 0 | tee -a $dst
		echo "##########################################################" | tee -a $dst
	done
echo "done"
