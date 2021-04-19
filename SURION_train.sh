echo "Training custom yolov4 detector"

data="cfg/surionOI_02.data"
config="cfg/yolov3_surionOI_pv_v02.cfg"
weights="/home/intel2/surion/dev/darknet/backup/yolov3_surionOI_pv_v02_30000.weights"

#Train yolov
#------------------------------
./darknet detector train $data $config $weights -map

data1="cfg/surionOI_01.data"
config1="cfg/yolov3_surionOI_pv_v01.cfg"
weights1="/home/intel2/surion/dev/darknet/backup/yolov3_surionOI_pv_v01_last.weights"

./darknet detector train $data1 $config1 $weights1 -map

#=====================================================================================================
