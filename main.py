import image_segmentation as s
from PIL import Image
import numpy as np

image = Image.open('image.jpg').convert('L')

imageData = np.asarray(image)

binarizedImageData = s.binarize(imageData, s.otsu(imageData))

Image.fromarray(binarizedImageData).convert('RGB').save('binarized_image.jpg')