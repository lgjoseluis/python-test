#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

import io

#Install: pip install requests
import requests

#Install: pip install Pillow
from PIL import Image
from PIL.ExifTags import TAGS

class ImageInformation:

    def __init__(self, urlImage):
        self.urlImage = urlImage

    def ShowMetadata(self):
        response = requests.get(self.urlImage)
        image_data = response.content

        image = Image.open(io.BytesIO(image_data))

        exif_data = image._getexif()
        
        if exif_data != None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print('Can\'t get information!')