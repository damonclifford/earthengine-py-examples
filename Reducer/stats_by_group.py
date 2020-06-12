import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Load a collection of US census blocks.
blocks = ee.FeatureCollection('TIGER/2010/Blocks')

# Compute sums of the specified properties, grouped by state code.
sums = blocks \
  .filter(ee.Filter.And(
    ee.Filter.neq('pop10', {}),
    ee.Filter.neq('housing10', {}))) \
  .reduceColumns(**{
    'selectors': ['pop10', 'housing10', 'statefp10'],
    'reducer': ee.Reducer.sum().repeat(2).group(**{
      'groupField': 2,
      'groupName': 'state-code',
    })
})

# Print the resultant Dictionary.
print(sums.getInfo())

# Display the map.
Map
