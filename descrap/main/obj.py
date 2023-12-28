import cv2
from datetime import datetime
from django.templatetags.static import static
def objd(path):
	date = datetime.now()
	name= date.strftime('%H:%M')


	img = cv2.imread(path)
	classNames = []
	identified = []
	pricing = {
				"LAPTOP": "300",
				"MOBILE": "200",
				"CLOCK": "40",
				"MICROVAWE"	: "500",
				"CELL PHONE" : "200",
				"OVEN" : "400",
				"REFRIGERATOR" : "2000",
				"KEYBOARD" : "50",
				"TV" : "4000",
				"MOUSE":"50"
			}
	classFile = './datasets/coco.names'
	with open(classFile,'rt') as f:
				classNames = f.read().rstrip('\n').split('\n')
				
	configPath = './datasets/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
	weightsPath = './datasets/frozen_inference_graph.pb'
	net = cv2.dnn_DetectionModel(weightsPath,configPath)
	net.setInputSize(320,320)
	net.setInputScale(1.0/ 127.5)
	net.setInputMean((127.5, 127.5, 127.5))
	net.setInputSwapRB(True)

	classIds, confs, bbox = net.detect(img,confThreshold=0.7)

	if len(classIds) != 0:
				for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
					cv2.rectangle(img,box,color=(0,255,0),thickness=2)
					cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
					cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
					identified.append(classNames[classId-1].upper())
					
	cv2.imwrite("ack.png",img)
	# print(identified)

		# Loop through the items in identified and calculate the total price and show the price of each item in front of it
	total = 0
	finalprice = []
	no_item = len(identified)
	for item in identified:
			if item in pricing:
				finalprice.append(pricing[item])
				total += int(pricing[item])
			else:
				continue
	# print(total)
	# print(finalprice)
	# print(no_item)
	return identified,finalprice,total,no_item,
	

	

