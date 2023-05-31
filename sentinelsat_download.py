# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

api = SentinelAPI('dualtaofionnagain', 'zed5GfUG8mVG!tU', 'https://scihub.copernicus.eu/dhus/')

lon, lat = -16.26, 16.30

footprint = f'POINT({lon} {lat})'
product_type = 'GRD'
date_start = date(2023, 4, 1)  # Example: start date
date_end = date(2023, 4, 30)  # Example: end date

# # Search for products
# products = api.query(footprint, date=(date_start, date_end), producttype=product_type)

# # download single scene by known product id
# api.download(<product_id>)

# search by polygon, time, and SciHub query keywords
# footprint = geojson_to_wkt(read_geojson('/path/to/map.geojson'))
products = api.query(footprint,
                     date=(date_start, date_end),
                     platformname='Sentinel-1')

# Print the available products
print("Available Products:")
for product in products:
    print(f"Product ID: {product}, Date: {products[product]['beginposition']}")

# # download all quicklooks
# api.download_all_quicklooks(products, directory_path='.', n_concurrent_dl=4)

# download all results from the search
api.download_all(products)

# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

# GeoJSON FeatureCollection containing footprints and metadata of the scenes
api.to_geojson(products)

# GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
api.to_geodataframe(products)

# # Get basic information about the product: its title, file size, MD5 sum, date, footprint and
# # its download url
# api.get_product_odata(<product_id>)

# # Get the product's full metadata available on the server
# api.get_product_odata(<product_id>, full=True)