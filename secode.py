#!/usr/bin/env python
# coding=utf-8
import pytesseract
from PIL import Image
image=Image.open('./image.jpg')
vcode =pytesseract.image_to_string(image)
print (vcode)
