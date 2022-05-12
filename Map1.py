import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My App")
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="It is me",icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("MapDhake.html")