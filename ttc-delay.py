import requests
import pandas as pd
import openpyxl

# # Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# # https://docs.ckan.org/en/latest/api/

# # To hit our API, you'll be making requests to:
# base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# # Datasets are called "packages". Each package can contain many "resources"
# # To retrieve the metadata for this package and its resources, use the package name in this page's URL:
# url = base_url + "/api/3/action/package_show"
# params = { "id": "ttc-subway-delay-data"}
# package = requests.get(url, params = params).json()

# # To get resource data:
# l_of_dfs = []

# for idx, resource in enumerate(package["result"]["resources"]):

#        # To get metadata for non datastore_active resources:
#        if not resource["datastore_active"]:
#            url = base_url + "/api/3/action/resource_show?id=" + resource["id"]
#            resource_metadata = requests.get(url).json()

#            if resource_metadata['result']['name'] not in ["ttc-subway-delay-codes", "ttc-subway-delay-data-readme"]:
#                   print(resource_metadata['result']['name'])
#                   df = pd.read_excel(resource_metadata['result']['url'])
#                   l_of_dfs.append(df)
#               # From here, you can use the "url" attribute to download this file

# final_df = pd.concat(l_of_dfs)
# final_df.to_csv("all_delays.csv")

pd.set_option('display.max_columns', 500)

delay_df = pd.read_csv("all_delays.csv")
codes_df = pd.read_csv("TTCDelayCodes.csv")

codes_df.columns = ['Code', 'CodeDescription', 'Type'] 

ttc_df = pd.merge(left=delay_df, right=codes_df, on='Code', how='left')
print(ttc_df.head())