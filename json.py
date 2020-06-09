import json
string ='''
{"people":23,
 "engineer":10,
 "skills":{"ce": 5,
         "me":5
        }
}
'''

python_object = json.loads(string)
del python_object['skills']['ce']

string_revised = json.dumps(python_object, indent=1)

with open('example_1.json') as f:
    python_object = json.load(f)

with open('new_json.json', 'w') as f:
    json.dump(python_object, f, indent=2)

#%% handeling csv file
import os
import pandas as pd
df = pd.read_csv('iris.csv')

output_type = ['split', 'records', 'index', 'columns', 'values', 'table', 'columns']
for orient in output_type:
    df.to_json('df_json.json', orient= orient)
    
    with open('df_json.json', 'r') as f:
        python_object = json.load(f)
    with open('df_json.json', 'w') as f:
        json.dump(python_object, f, indent=2)       
    print(orient, os.path.getsize('df_json.json'))

print(python_object['feature1']['10'])

#%% real world example with json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))
