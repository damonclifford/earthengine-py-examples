
#!/usr/bin/env python
"""FeatureCollection Join example.

Show parks in San Francisco within 2 kilometers of a BART station.
"""

import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

Map.setCenter(-122.45, 37.75, 13)

bart = ee.FeatureCollection('GOOGLE/EE/DEMOS/bart-locations')
parks = ee.FeatureCollection('GOOGLE/EE/DEMOS/sf-parks')
buffered_bart = bart.map(lambda f: f.buffer(2000))

join_filter = ee.Filter.withinDistance(2000, '.geo', None, '.geo')
close_parks = ee.Join.simple().apply(parks, bart, join_filter)

Map.addLayer(buffered_bart, {'color': 'b0b0b0'}, "BART Stations")
Map.addLayer(close_parks, {'color': '008000'}, "Parks")

# Display the map.
Map
