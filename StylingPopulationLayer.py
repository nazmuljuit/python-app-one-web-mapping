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

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My App")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el) + " m",fill_color=color_procedure(el),color='gray',fil_opacity=.07))
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.save("Map.html")