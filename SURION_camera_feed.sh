echo "Test network on rtsp stream"
echo $1
echo "Threshold" $2
sleep 2s

data="cfg/yolov4_Surion_OI_2.data"
config="cfg/yolov4_Surion_OI_2.cfg"
weights="/home/ryzen1/Surion/darknet/backup/yolov4_Surion_OI_2_best.weights"

case $1 in
	"Office")
		./darknet detector demo $data $config $weights rtsp://admin:surionDev@192.168.0.33:554/profile1 -thresh $2
	;;
	"Road")
		./darknet detector demo $data $config $weights  rtsp://admin:surionDev@192.168.0.31:554/profile1 -thresh $2
	;;
	"Door")
		./darknet detector demo $data $config $weights  rtsp://admin:surionDev@192.168.0.30:554/profile1 -thresh $2
	;;
esac


