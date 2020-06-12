import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# add some data to the Map
dem = ee.Image("AHN/AHN2_05M_RUW")
Map.addLayer(dem, {'min': -5, 'max': 50, 'palette': ['000000', 'ffffff'] }, 'DEM', True)

# zoom in somewhere
Map.setCenter(4.4585, 52.0774, 14)

# TEST
center= Map.getCenter()

# add bounds to the map
Map.addLayer(center, { 'color': 'red' }, 'center')

# Display the map.
Map
