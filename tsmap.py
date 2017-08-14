import folium
import vincent
import pandas

def createTSMap(pos, timeSeries, zoom_start=4):
    map = folium.Map(location=pos.items(), zoom_start=4,crs='EPSG4326')

    df = timeSeries;
    df.index = df.index.values.astype('M8[D]')
    chart = vincent.Line(df[['evi','ndvi']],width=300,height=150)
    chart.legend(title='')
    chart.axis_titles(x='dates', y='')

    popup = folium.Popup(max_width=400)
    folium.Vega(chart.to_json(), height=200, width=450).add_to(popup)
    folium.Marker(pos.items(), popup=popup,icon=folium.Icon(color='green',icon='info-sign')).add_to(map)

    wms = folium.features.WmsTileLayer('https://neo.sci.gsfc.nasa.gov/wms/wms',
                                       name='MODIS Data',
                                       format='image/png',
                                       layers='MOD13A2_M_NDVI')
    wms.add_to(map)
    return map
