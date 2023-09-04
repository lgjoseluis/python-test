#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Packages
import argparse

from WebScraping import ImageMetadata

parser = argparse.ArgumentParser(description="Get image information.")
parser.add_argument('-t', '--target', help="Target image")
parser = parser.parse_args()

def GetImageInformation(urlImage):    
    info = ImageMetadata.ImageInformation(urlImage)
    info.ShowMetadata()

def main():
    if parser.target:
        GetImageInformation(parser.target)
    else:
        print("The target image is required.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Break execute.")
    finally:
        print("End execute.")