!nvidia-smi

----------------------------------------

import os
HOME = os.getcwd()
print(HOME)

---------------------------------------

!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()


from ultralytics import YOLO

from IPython.display import display, Image

-------------------------------------

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Personel API Key")
project = rf.workspace("Account Name").project("Project")
dataset = project.version(1).download("Yolo Version")

------------------------------------


%cd {HOME}

!yolo task=segment mode=train model=yolov8s-seg.pt data={"dataset"} epochs=50 imgsz=800 plots=True



!ls {HOME}/runs/segment/train/



%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/confusion_matrix.png', width=600)



%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/results.png', width=600)



%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/val_batch0_pred.jpg', width=1000)



%cd {HOME}

!yolo task=segment mode=val model={HOME}"Model Directory" data={"dataset path"}



%cd {HOME}
!yolo task=segment mode=predict model={HOME}"Model Directory" conf=0.32 source="Test image path" save=True



import glob
from IPython.display import Image, display



for image_path in glob.glob(f'{HOME}/runs/segment/predict/*.jpg')[5:30]:
      display(Image(filename=image_path, width=600))
      print("\n")



















