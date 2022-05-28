import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])

def color_procedure(elevation):
  if elevation < 1000:
    return 'black'
  elif 1000 <= elevation < 3000:
    return 'red'
  else:
    return 'blue'

map = folium.Map(location=[38.58,-99.09],zoom_start=3,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el) + " m",fill_color=color_procedure(el),color='gray',fil_opacity=.07))
fgp = folium.FeatureGroup(name="Populations")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")