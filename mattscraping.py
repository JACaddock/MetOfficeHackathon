from bs4 import BeautifulSoup
import urllib.request
api_key = 'bb2a1f77-5607-4015-bca7-1d3d7c70d11f'
url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/datatype/sitelist?key='+ api_key

req = urllib.request.urlopen(url)

xml = BeautifulSoup(req, 'xml')

for location in xml.findAll('Locations'):
    for attribute in location.findAll("Location"):
        print(attribute['latitude'], attribute['name'])


