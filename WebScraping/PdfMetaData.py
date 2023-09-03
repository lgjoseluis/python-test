#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

import io
import urllib.request

#Beautiu
from bs4 import BeautifulSoup

#Install: pip install pypdf
from pypdf import PdfReader

class PdfInfo:
    PdfDocuments = []

    def __init__(self, webSite):
        self.webSite = webSite

    def __getDocuments(self):
        site = urllib.request.urlopen(self.webSite)
        
        soup = BeautifulSoup(site, "html.parser")

        links = soup('a')

        for l in links:
            link = l.get('href')           
            
            if link != None and link.find("pdf") > 0:
                self.PdfDocuments.append(link)

    def ShowMetaData(self):
        self.__getDocuments()

        for doc in self.PdfDocuments:
            response = urllib.request.urlopen(doc)
            obj_mem = io.BytesIO(response.read())
            
            reader = PdfReader(obj_mem)
            meta = reader.metadata

            print('From: ', doc)
            print('Title:', meta.title)
            print('Subject:', meta.subject)
            print('Number of pages:', len(reader.pages))
            print('Author:', meta.author)
            print('Creator:', meta.creator)
            print('Producer:', meta.producer)  
            print('Creation date:', meta.creation_date)  
            print('Modification date:', meta.modification_date)  

            print('\n')


        

        