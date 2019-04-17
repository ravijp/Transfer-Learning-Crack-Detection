# Classifying-defected-parts

## How to predict using the model:- 
To predict on new image or folder of images, please provide path in --images_path and excute the below command. 

```
python ./label_image.py \
--images_path={Path of the Image file} \
--trained_model_path = /model_v7.h5 \
--incept_model_path = /incept_model.h5 
```

The trained model achieved *~88 %* accuracy with following parameters :- 
- Epochs = 100
- Batch size = 32
- Learning Rate = 1e-5 (RMSprop)

