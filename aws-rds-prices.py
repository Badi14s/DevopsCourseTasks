import requests
import json
import sys

DB_TYPE_TO_SEARCH = 'db.t3'

base_url = 'https://pricing.us-east-1.amazonaws.com'
region_index = requests.get(base_url + "/offers/v1.0/aws/AmazonRDS/current/region_index.json").json()

regions = region_index['regions']
af_south_1_json = regions['af-south-1']
af_south_1_url = af_south_1_json['currentVersionUrl']
region_index = requests.get(base_url + af_south_1_url).json()

for term_name, term in region_index['terms']['OnDemand'].items():
    details = list(term.values())[0]
    price_details = list(details['priceDimensions'].values())[0]
    description, price = price_details['description'], price_details['pricePerUnit']['USD']
    if DB_TYPE_TO_SEARCH in description:
        print(f'{price}, {description}')
