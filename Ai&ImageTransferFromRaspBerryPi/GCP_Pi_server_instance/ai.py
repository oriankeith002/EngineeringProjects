from roboflow import Roboflow
import cv2 
import numpy as np
from ultralytics import YOLO


def roboflow_model():
	rf = Roboflow(api_key="ZhikyKdKaVCJN7Svfdqx")
	project = rf.workspace().project("egg-detection-final")
	model = project.version(3).model
	return model 


def ultralytics_model(filename="yolov8s.pt"):
    model = YOLO(filename)
    return model

def cv2_decoder(image_data):
	image = cv2.imdecode(
		np.frombuffer(
			image_data.getvalue(), dtype=np.uint8
			), 
		cv2.IMREAD_UNCHANGED)
	return image

def ultralytics_predict(model, img_stream):
        image = cv2_decoder(img_stream)
        result = model.predict(image)
        return result, len(result[0].boxes.data)

def save_stream_to_file(img_stream):
       image = cv2_decoder(img_stream)
       cv2.imwrite('Received_Image.png',image)

def roboflow_predict(model, img_stream):
        # image = cv2_decoder(img_stream)
        save_stream_to_file(img_stream) # saving image stream to a file.
        im = cv2.imread('Received_Image.png') # read as ndarray
        result = model.predict(im, confidence=40, overlap=30).json()
        for bounding_box in result['predictions']:
                x0 = bounding_box['x'] - bounding_box['width']/2
                x1 = bounding_box['x'] + bounding_box['width']/2
                y0 = bounding_box['y'] - bounding_box['height']/2
                y1 = bounding_box['y'] + bounding_box['height']/2

                start_point = (int(x0),int(y0))
                end_point = (int(x1),int(y1))

                cv2.rectangle(im,start_point,end_point,color=(0,0,0), thickness=1)
                cv2.putText(
                                im,
                                bounding_box["class"],
                                (int(x0),int(y0) - 10),
                                fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale= 0.6,
                                color=(255,255,255),
                                thickness=2
                                )
                # saving image with bounding boxes
                cv2.imwrite("Plotted_Detections.jpg",im) 

        return result, len(result["predictions"])


def save_file(img_stream):
    with open("idiot.png", "wb") as f:
        f.write(img_stream.getbuffer())
