#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

import pygeoip

class GeoIpInformation:
    def __init__(self, domainName, ipAddress):
        self.DomainName = domainName
        self.IpAddress = str(ipAddress)

    def __IpInformation(self):
        gi = pygeoip.GeoIP('GeoLiteCity.dat')
        data = gi.record_by_addr(self.IpAddress)
        
        print('Country'.ljust(10, '.'), '{} ({})'.format(data['country_name'], data['country_code']))        
        print('City'.ljust(10,'.'), '{} ({})'.format(data['city'], data['postal_code']))
        print('GPS'.ljust(10,'.'), '({}, {})'.format(data['latitude'], data['longitude']) )

    def GetIpInformation(self):
        title = "Geolocalization {}".format(self.IpAddress)

        print (title.center(50,'='))

        self.__IpInformation()