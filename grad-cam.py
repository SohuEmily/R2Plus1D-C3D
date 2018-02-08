import cv2
import numpy as np
from torchvision import models

import utils2

if __name__ == '__main__':
    grad_cam = utils2.GradCam(model=models.vgg19(pretrained=True), target_layer=35)

    img = cv2.imread('both.png', 1)
    img = np.float32(cv2.resize(img, (224, 224))) / 255
    input = utils2.preprocess_image(img)

    # If None, returns the map for the highest scoring category.
    # Otherwise, targets the requested index.
    target_index = None

    mask = grad_cam(input, target_index)

    utils2.show_cam_on_image(img, mask)
