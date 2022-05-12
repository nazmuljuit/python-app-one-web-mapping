import folium
map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Stamen Terrain")
#map = folium.Map(location=[23.81,90.41],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My App")
for cordinates in [[23.86,90.38],[23.60,89.83]]:
    fg.add_child(folium.Marker(location=cordinates,popup="It is me",icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("MapDhake.html")