from bs4 import BeautifulSoup
import urllib.request
api_key = 'bb2a1f77-5607-4015-bca7-1d3d7c70d11f'
#url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/datatype/sitelist?key='+ api_key

#req = urllib.request.urlopen(url)

#xml = BeautifulSoup(req, 'xml')
class Location:
    def __init__(self, name, lat, long, feelslike, windgust, humidity, temp, visibility, winddir, windspeed, maxuvindex, weathertype, precipprob):
        self.name = name
        self.lat = lat
        self.long = long
        self.feelslike = feelslike
        self.windgust = windgust
        self.humidity = humidity
        self.temp = temp
        self.visibility = visibility
        self.winddir = winddir
        self.windspeed = windspeed
        self.maxuvindex = maxuvindex
        self.weathertype = weathertype
        self.precipprob = precipprob


def load_info(location_name):
    url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/sitelist?key='+api_key
    req = urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'xml')
    for location in xml.findAll('Locations'):
        for attribute in location.findAll('Location'):
            if attribute['name'] == location_name:
                id = attribute['id']
                lat = attribute['latitude']
                long = attribute['longitude']

                url2 = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/'+id+'?res=3hourly&key='+api_key
                req2 = urllib.request.urlopen(url2)
                xml2 = BeautifulSoup(req2, 'xml')
                attributes = xml2.find("SiteRep").find("DV").find("Location").find("Period").find("Rep")
                feelslike = attributes['F']
                windgust = attributes['G']
                humidity = attributes['H']
                temp = attributes['T']
                visibility = attributes['V']
                winddir = attributes['D']
                windspeed = attributes['S']
                maxuvindex = attributes['U']
                weathertype = attributes['W']
                precipprob = attributes['Pp']
                newlocation = Location(location_name, lat, long, feelslike, windgust, humidity, temp, visibility, winddir, windspeed, maxuvindex, weathertype, precipprob)
                return newlocation

def return_all(loc_name):
    loc = load_info(loc_name)
    att = {
        "Name" : loc.name,
        "Latitude" : loc.lat,
        "Lonitude" : loc.long,
        "Feels Like" : loc.feelslike,
        "Wind Gust" : loc.windgust,
        "Humidity" : loc.humidity,
        "Temperature" : loc.temp,
        "Visibility" : loc.visibility,
        "Wind Direction" : loc.winddir,
        "Wind Speed" : loc.windspeed,
        "Max UV Index" : loc.maxuvindex,
        "Weather Type" : loc.weathertype,
        "Precipitation Probability" : loc.precipprob

    }

    return att

if __name__ == "__main__":
    loc = load_info("Killowen")
    print(loc.winddir)
    
    locs = return_all("Killowen")
    for key, value in locs.items():
        print(key," = ", value)
