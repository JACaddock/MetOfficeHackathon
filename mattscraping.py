from bs4 import BeautifulSoup
import urllib.request
api_key = 'bb2a1f77-5607-4015-bca7-1d3d7c70d11f'
#url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/datatype/sitelist?key='+ api_key

#req = urllib.request.urlopen(url)

#xml = BeautifulSoup(req, 'xml')
class location:
    def __init__(self, name, lat, long, country, feelslike):
        self.name = name
        self.lat = lat
        self.long = long
        self.feelslike = feelslike
        self.country = country

def load_info(location_name):
    url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/sitelist?key='+api_key
    req = urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'xml')
    for location in xml.findAll('Locations'):
        for attribute in location.findAll('Location'):
            if attribute['name'] == location_name:
                id = attribute['id']
                url2 = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/'+id+'?key='+api_key
                

