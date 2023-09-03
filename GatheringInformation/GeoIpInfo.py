#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Install: pip install pygeoip
#import pygeoip

#Install: pip install 2ip
#from twoip import TwoIP

import socket
import requests
#ip2geotools: pip install ip2geotools
from ip2geotools.databases.noncommercial import DbIpCity
#from geopy.distance import distance

class GeoIpInformation:
    def __init__(self, domainName, ipAddress):
        self.DomainName = domainName
        self.IpAddress = str(ipAddress)

    #pygeoip
    def __IpInformationByGeoIp(self):
        gi = pygeoip.GeoIP('GeoLiteCity.dat')
        data = gi.record_by_addr(self.IpAddress)
        
        print('Country'.ljust(10, '.'), '{} ({})'.format(data['country_name'], data['country_code']))        
        print('City'.ljust(10,'.'), '{} ({})'.format(data['city'], data['postal_code']))
        print('GPS'.ljust(10,'.'), '({}, {})'.format(data['latitude'], data['longitude']) )

    #2ip
    def __IpInformationBy2Ip(self):
        twoip = TwoIP(key = None)
        pr = twoip.provider(ip = self.IpAddress, format = 'json')

        #print(providerResult.name_ripe)
        #print(providerResult.site)        

        gip = twoip.geo(ip = self.IpAddress)

        print(gip)

    #ip2geotools
    def __IpInformationGeoTools(self):
        res = DbIpCity.get(self.IpAddress, api_key="free")
        print(res)

    def __IpInformation(self):
        res = requests.get(f'https://ipapi.co/{self.IpAddress}/json/').json()
        
        print('IP'.ljust(22,'-'), f"{res['ip']} - {res['network']} ({res['version']})")
        print('Country'.ljust(22,'-'), f"{res['country_capital']},  {res['country']} {res['country_name']} ({res['country_code']}|{res['country_code_iso3']})")
        #print(f"IP Address: {res.continent_code}")
        #print(f"IP Address: {res.in_eu}")
        print('City'.ljust(22,'-'), f"{res['city']}, {res['region']} ({res['region_code']})")
        print('Postal'.ljust(22,'-'), res['postal'])
        print('Latitude'.ljust(22,'-'), res['latitude'])
        print('Longitude'.ljust(22,'-'), res['longitude'])
        print('Timezone'.ljust(22,'-'), f"{res['timezone']} ({res['utc_offset']})")
        print('Country calling code'.ljust(22,'-'), res['country_calling_code'])
        print('Currency'.ljust(22,'-'), f"{res['currency_name']} ({res['currency']})")
        print('Language'.ljust(22,'-'), res['languages'])
        #print(f"area: {res['country_area']}")
        #print(f"population: {res['country_population']}")
        print('asn'.ljust(22,'-'), res['asn'])
        print('org'.ljust(22,'-'), res['org'])
        print('country_tld'.ljust(22,'-'), res['country_tld'])

    def GetIpInformation(self):
        title = "Geolocalization {}".format(self.IpAddress)

        print (title.center(50,'='))

        #self.__IpInformationBy2Ip()
        #self.__IpInformationGeoTools()
        self.__IpInformation()