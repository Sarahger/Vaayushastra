import requests

key='3da7Sj55jOVAeqUzvNwUidntY9V24VwB'
url='https://www.mapquestapi.com/geocoding/v1/address'
loc='Bandstand, Bandra'
main_url= url + key + '&location' + loc
print(main_url)

r = requests.get(main_url)
data = r.json()['results'][0]
location = data['locations'][0]
city = location['adminArea5']
state = location['adminArea3']
country = location['adminArea1']
zipcode= location['postalCode']
lat = location['latLng']['lat']
lng = location['latLng']['lng']

print('City : ',city)
print('State : ',state)
print('Country : ',country)
print('Postal code : ',zipcode)
print('Latitude : ',lat)
print('Longitude : ',lng)