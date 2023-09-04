#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Packages
import argparse

#Local packages
from GatheringInformation import DnsInfo, WhoisInfo, GeoIpInfo
#from GatheringInformation import WhoisInfo
#from GatheringInformation import GeoIpInfo

parser = argparse.ArgumentParser(description="Get information for a domain.")
parser.add_argument('-t', '--target', help="Domain target")
parser = parser.parse_args()

def LaunchProcessGathering(nameDomain):
    # print ("*".center(50,'*'))
    # print (nameDomain.center(50,' '))
    # print ("*".center(50,'*'), '\n')

    objDnsInfo = DnsInfo.DnsInformation(nameDomain)
    objDnsInfo.GetDnsInformation()
    ipV4 = objDnsInfo.GetIpv4ForDomain()

    objWhoisInfo = WhoisInfo.DomainInformation(nameDomain)
    objWhoisInfo.GetDomainInformation(2)

    if ipV4 != None:
        objGeoIpInfo = GeoIpInfo.GeoIpInformation(nameDomain, ipV4)
        objGeoIpInfo.GetIpInformation()
    else:
        print('Can\'t get IP!')

def main():
    if parser.target:
        LaunchProcessGathering(parser.target)
    else:
        print("The domain target is required.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Break execute.")
    finally:
        print("End execute.")