#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Packages
import argparse

from WebScraping import PdfMetaData

parser = argparse.ArgumentParser(description="Get PDF information from a website.")
parser.add_argument('-t', '--target', help="Target website")
parser = parser.parse_args()

def GetPdfInformation(webSite):    
    info = PdfMetaData.PdfInfo(webSite)
    info.ShowMetaData()

def main():
    if parser.target:
        GetPdfInformation(parser.target)
    else:
        print("The target website is required.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Break execute.")
    finally:
        print("End execute.")