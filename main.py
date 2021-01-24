import os
from PIL import Image

# Specify the directory where images are present
PATH = 'path/to/images'

entries = os.listdir(PATH)
imgList = []
for entry in entries:
    if(entry != entries[0]):
        img = Image.open(PATH + entry)
        imgList.append(img.convert('RGB'))

pdf = Image.open(PATH + entries[0]).convert('RGB')

pdf.save(PATH + "output.pdf", save_all=True, append_images=imgList)
