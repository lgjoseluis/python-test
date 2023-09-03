#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Install: pip install python-whois
import whois

class DomainInformation:
    
    def __init__(self, domainName):
        self.domainName = domainName

    def __WhoisInformation(self):
        print ('Domain name', self.domainName)
        result = whois.whois(self.domainName)
        
        print('Creation date'.ljust(18, '.'),result.creation_date)
        print('Expiration date'.ljust(18,'.'), result.expiration_date)
        print('Last update'.ljust(18,'.'), result.last_updated)
        print('Name'.ljust(18,'.'), result.name)
        print('Name servers'.ljust(18,'.'), result.name_servers)
        print('Registrar'.ljust(18,'.'), result.registrar)
    
    #def __PyWhoisInformation(self):
        #result = pythonwhois.get_whois(self.domainName)
        #print(result)

    def GetDomainInformation(self, typeInfo):
        title = "Whois Records"

        print (title.center(50,'='))
        
        #if typeInfo == 2:
        self.__WhoisInformation()
        #else:
        #self.__PyWhoisInformation()
