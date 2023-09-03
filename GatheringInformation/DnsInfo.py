#!/usr/bin/env/ python
#_*_ coding: utf8 _*_

#install: pip install dnspyhton (lasted version)
import dns.resolver  

class DnsInformation:

    def __init__(self, domainName):
        self.domainName = domainName

    def __DnsResolver(self, domainName):    
        rDataType=['CNAME','A', 'AAAA','NS', 'SOA', 'OPT', 'MX', 'PTR', 'SRV', 'TXT']
        
        #print(answer.response.to_text())

        for dataType in rDataType:
            try:
                answer = dns.resolver.query(domainName, dataType, raise_on_no_answer=False)
                
                if answer is not None:
                    for data in answer:
                        print(dataType.ljust(8,'.'), data)
            except Exception as e:
                print(dataType.ljust(8,'.'), e)        

    def GetDnsInformation(self):
        title = "DNS Query"

        print (title.center(50,'='))
        
        self.__DnsResolver(self.domainName)

    def GetIpv4ForDomain(self):
        try:
            data = '0.0.0.0'

            answer = dns.resolver.query(self.domainName, 'A')

            if answer is not None:
                for ipval in answer:
                    data = ipval.to_text()
            
            return data
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return '0.0.0.0'