from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import glob
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
from tensorflow.keras.models import load_model
# import model_evaluation_utils as meu
import sys

# sys.path.insert(0, 'Downloads/')

def get_bottleneck_features(model, input_imgs):
    features = model.predict(input_imgs, verbose=0)
    return features

def read_images(test_files, IMG_DIM=(224, 224)):
    test_imgs = [img_to_array(load_img(img, target_size=IMG_DIM)) for img in test_files]
    test_imgs = np.array(test_imgs)

    test_imgs_scaled = test_imgs.astype('float32')
    test_imgs_scaled /= 255
    
    return test_imgs_scaled

if __name__ == "__main__":
    trained_model_path = 'Downloads/model_v7.h5'
    incept_model_path = 'Downloads/incept_model.h5'
    images_path = 'Downloads/Test/'
    

    parser = argparse.ArgumentParser()
    parser.add_argument("--images_path", help="Image/Folder containing images to be processed")
    parser.add_argument("--trained_model_path", help="graph/model to be executed")
    parser.add_argument("--incept_model_path", help="Inception model to get bottleneck features")
    args = parser.parse_args()
    
    if args.images_path:
        images_path = args.images_path
    if args.trained_model_path:
        trained_model_path = args.trained_model_path
    if args.incept_model_path:
        incept_model_path = args.incept_model_path
    
    if '.jpg' in images_path:
        test_files = [images_path]
    else:
        test_files = glob.glob(images_path + '/*/*.jpg')
    
    incept_model = load_model(incept_model_path)
    trained_model = load_model(trained_model_path)

    print('Reading images')
    test_imgs_scaled = read_images(test_files)
    print('Getting Bottleneck features')
    test_bottleneck_features = get_bottleneck_features(incept_model, test_imgs_scaled)
    
    class2num_label_transformer = lambda l: [0 if 'Crack_and_Wrinkle' in x else 1 for x in l]
    num2class_label_transformer = lambda l: ['Defective' if x == 1 else 'Healthy' for x in l]
    print('Start predicting...')
    predictions = trained_model.predict_classes(test_bottleneck_features, verbose=0)
    predictions = num2class_label_transformer(predictions)

    for i, p in enumerate(predictions):
        print(f'For image {i}, model predicts it to be {predictions[i]}')
    