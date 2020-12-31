import requests
import json
import sys

base_url = 'https://pricing.us-east-1.amazonaws.com'
r = requests.get(base_url+"/offers/v1.0/aws/AmazonRDS/current/region_index.json") 
json_reponse = r.json()
json_regions = json_reponse['regions']
af_south_1_json = json_regions['af-south-1']
af_south_1_url = af_south_1_json['currentVersionUrl']
r = requests.get(base_url+af_south_1_url)
print(r.text)