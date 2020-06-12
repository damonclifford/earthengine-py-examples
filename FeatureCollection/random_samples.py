import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Define an arbitrary region in which to compute random points.
region = ee.Geometry.Rectangle(-119.224, 34.669, -99.536, 50.064)

# Create 1000 random points in the region.
randomPoints = ee.FeatureCollection.randomPoints(region)

# Display the points.
Map.centerObject(randomPoints)
Map.addLayer(randomPoints, {}, 'random points')

# Display the map.
Map
