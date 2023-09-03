#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Packages
import argparse

from WebScraping import LinkInformation

parser = argparse.ArgumentParser(description="Get information from a webpage.")
parser.add_argument('-t', '--target', help="Target website")
parser = parser.parse_args()

def GetLinksInformation(webSite):    
    info = LinkInformation.RetriveLinks(webSite)
    info.ShowLinks()


def main():
    if parser.target:
        GetLinksInformation(parser.target)
    else:
        print("The target website is required.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Break execute.")
    finally:
        print("End execute.")