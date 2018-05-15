import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

# creating the map object at some location
map = folium.Map(location=[50,-120],zoom_start = 6,tiles = "Mapbox Bright")

# get all the latitudes
lat = list(data["LAT"])
# get all the longitudes
lon = list(data["LON"])
# get the elevation
elev = list(data["ELEV"])

def color_generator(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000<=elevation<=3000:
		return 'orange'
	else:
		return 'red'

#we can add markers to identify interested locations
# create a featureGroup object and intialize it
fg = folium.FeatureGroup(name = "My Map")

# taking the cordinates from the volcanoes textfile in the folder and marking them red
# the code is for adding location shaped markers

# for lt,ln,el in zip(lat,lon,elev):
# 	fg.add_child(folium.Marker(location=[lt,ln], popup = folium.Popup(str(el)+" m",parse_html=True) ,icon = folium.Icon(color=color_generator(el))))
# map.add_child(fg)

# code for adding circle shaped markers
for lt,ln,el in zip(lat,lon,elev):
	fg.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup = folium.Popup(str(el)+" m",parse_html=True) ,fill_color=color_generator(el),fill = True, color = 'grey',fill_opacity = 0.7))




# adding multiple markers
# for coordinates in [[30,-96],[28,-94]]:
# 	fg.add_child(folium.Marker(location=coordinates,popup="Hi I am also a Marker",icon = folium.Icon(color="green")))
# map.add_child(fg)	

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
	style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
	else 'orange' if 100000000 <=x['properties']['POP2005']<20000000 
	else 'red'}))


map.add_child(fg)

map.add_child(folium.LayerControl())
map.save("Map1.html")

