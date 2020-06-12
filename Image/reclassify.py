
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('USGS/NLCD/NLCD2016')
landcover = ee.Image(dataset.select('landcover'))

# https:#developers.google.com/earth-engine/datasets/catalog/USGS_NLCD
# combine all Developed land classes as one class
inList = ee.List([21, 22, 23, 24])
outList = ee.List.repeat(20, inList.size())

reclassified = landcover.remap(inList, outList)

landcoverVis = {
  'min': 0.0,
  'max': 95.0,
  'palette': [
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '466b9f',
    'd1def8',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'dec5c5',
    'd99282',
    'eb0000',
    'ab0000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'b3ac9f',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '68ab5f',
    '1c5f2c',
    'b5c58f',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'af963c',
    'ccb879',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'dfdfc2',
    'd1d182',
    'a3cc51',
    '82ba9e',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'dcd939',
    'ab6c28',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    '000000',
    'b8d9eb',
    '000000',
    '000000',
    '000000',
    '000000',
    '6c9fb8'
  ],
}

Map.setCenter(-73.28, 40.64, 10)
Map.addLayer(landcover, landcoverVis, 'Landcover original')
Map.addLayer(reclassified, landcoverVis, 'Landcover reclassified')

# Display the map.
Map
