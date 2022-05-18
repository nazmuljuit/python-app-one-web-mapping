import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My App")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el) + " m",icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("Map.html")