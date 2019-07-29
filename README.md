# Classifying-defected-parts

## How to predict using the model:- 
To predict on new image or folder of images, please provide path in --images_path and excute the below command. 

```
python ./label_image.py \
--images_path={Path of the Image file or Folder of images} \
--trained_model_path = ./model_v7.h5 \
--incept_model_path = ./incept_model.h5 
```
An example on how to run this in a windows system with Anaconda : 
``` 
C:/ProgramData/Anaconda3/envs/tensorflow/python.exe "c:/Users/Panda/Downloads/Upload_Github/label_image.py" --images_path=C:/Users/Panda/Downloads/Test --trained_model_path=C:/Users/Panda/Downloads/Upload_Github/model_v7.h5 --incept_model_path=C:/Users/Panda/Downloads/Upload_Github/incept_model.h5
 ```


The trained model achieved *~88 %* accuracy with following parameters :- 
- Epochs = 100
- Batch size = 32
- Learning Rate = 1e-5 (RMSprop)

Ref:-
1. https://www.cse.ust.hk/~qyang/Docs/2009/tkde_transfer_learning.pdf
2. https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a
