FILE=`date '+%Y_%m_%d_%H_%M_%S_ec2.txt'`;
BASE_URL="https://pricing.us-east-1.amazonaws.com"
touch region_index.json
curl "$BASE_URL/offers/v1.0/aws/AmazonRDS/current/region_index.json" > region_index.json
af_south_1=$(jq '.regions."af-south-1".currentVersionUrl' region_index.json 2>&1 | sed 's/"//' | sed 's/"//')
curl "$BASE_URL$af_south_1" > $FILE