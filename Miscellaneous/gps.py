# # importing geopy library
# from geopy.geocoders import Nominatim

# # calling the Nominatim tool
# loc = Nominatim(user_agent="GetLoc")

# # entering the location name
# getLoc = loc.geocode("Gosainganj Lucknow")

# # printing address
# print(getLoc.address)

# # printing latitude and longitude
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude)




# from tkinter import *
# from geopy.geocoders import Nominatim

# # Create an instance of tkinter frame
# win = Tk()

# # Define geometry of the window
# win.geometry("700x350")

# # Initialize Nominatim API
# geolocator = Nominatim(user_agent="MyApp")

# # Latitude & Longitude input
# coordinates = "17.3850 , 78.4867"

# location = geolocator.reverse(coordinates)

# address = location.raw['address']

# # Traverse the data
# city = address.get('city', '')
# state = address.get('state', '')
# country = address.get('country', '')

# # Create a Label widget
# label1=Label(text="Given Latitude and Longitude: " + coordinates, font=("Calibri", 24, "bold"))
# label1.pack(pady=20)

# label2=Label(text="The city is: " + city, font=("Calibri", 24, "bold"))
# label2.pack(pady=20)

# label3=Label(text="The state is: " + state, font=("Calibri", 24, "bold"))
# label3.pack(pady=20)

# label4=Label(text="The country is: " + country, font=("Calibri", 24, "bold"))
# label4.pack(pady=20)

# win.mainloop()



# # Import the required library
# from geopy.geocoders import Nominatim

# # Initialize Nominatim API
# geolocator = Nominatim(user_agent="MyApp")

# location = geolocator.geocode("Mumbai")

# print("The latitude of the location is: ", location.latitude)
# print("The longitude of the location is: ", location.longitude)





from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("Nairobi, Kenya").raw
# print raw data
pprint(location)

