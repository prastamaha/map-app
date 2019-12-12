import folium, pandas

# Load CSV data
df = pandas.read_csv('data-sekolah.csv')
df.set_index('id', inplace=True)    # set id for index

lintang = list(df['lintang'])
bujur = list(df['bujur'])
sekolah = list(df['sekolah'])

popup = """
Sekolah: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""

def color_marker(jenis):
    if 'SMA' in jenis:
        return 'green'
    elif 'SMK' in jenis:
        return 'red'

# create map with default location on bali
map = folium.Map(location=[-8.573442, 115.194067])

# create feature group for parent of feature on map
fg = folium.FeatureGroup(name='SMA/SMK Denpasar MAP')

for l, b, s in zip(lintang, bujur, sekolah):
    iframe = folium.IFrame(html=popup % (s, s), width=100, height=100)
    fg.add_child(folium.Marker(location=[l,b],popup=folium.Popup(iframe), 
        icon=folium.Icon(color=color_marker(s))))

# add fg to map as child
map.add_child(fg)

# add map layer control
map.add_child(folium.LayerControl())

# save map to file named maps.html
map.save('map-app.html')