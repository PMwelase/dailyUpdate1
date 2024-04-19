# import requests
# import os

# LICENSE_KEY = "1B5D194B-A12144E7-8058EBE0-998709E3"
# eskom_url = 'https://developer.sepush.co.za/business/2.0/areas_nearby?lat=-26.150610&lon=28.031900'
# payload={}
# headers = {
#     'token': LICENSE_KEY,
# }

# # curl --location 'https://developer.sepush.co.za/business/2.0/topics_nearby?lat=-33.927330&lon=18.455440'
# response = requests.request("GET", eskom_url , headers=headers, data=payload)
# response = response.json()
# print(response)

data = "Hey"

# # Find Current Stage
# stage = int(response["events"][0]["note"][6])

# #Find all Affected Hours
# affected_hours = response["schedule"]["days"][0]["stages"][stage - 1]


# def all_affected_hours():
#     """Return all affected hours between 8am and 4pm"""
#     all_hours = []
#     for n in affected_hours:
#         if 8 <= int(n[0:2]) <= 16:
#             all_hours.append(n)

#     return all_hours



# if __name__ == "__main__":
#     print(all_affected_hours())
    