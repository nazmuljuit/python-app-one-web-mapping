import folium
map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[23.86,90.38],popup="Dhaka City",icon=folium.Icon(color="red")))
map.save("MapDhake.html")