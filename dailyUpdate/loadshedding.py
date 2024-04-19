import requests
import os
import json

LICENSE_KEY = "LICENSE KEY"

dbn_eskom_url = "https://developer.sepush.co.za/business/2.0/area?test&id=ethekwini3-12a-cbdeast"
cpt_eskom_url = "https://developer.sepush.co.za/business/2.0/area?id=capetown-7-foreshore"
jhb_eskom_url = "https://developer.sepush.co.za/business/2.0/area?id=jhbcitypower3-16-parkwoodeast"

payload={}
headers = {
    'token': LICENSE_KEY,
}

dbn_response = requests.request("GET", dbn_eskom_url , headers=headers, data=payload)
dbn_response = dbn_response.json()


cpt_response = requests.request("GET", cpt_eskom_url , headers=headers, data=payload)
cpt_response = cpt_response.json()


jhb_response = requests.request("GET", jhb_eskom_url , headers=headers, data=payload)
jhb_response = jhb_response.json()


try:    
    stage = int(dbn_response["events"][0]["note"][6])
    dbn_affected_hours = dbn_response["schedule"]["days"][0]["stages"][stage - 1]
    jhb_affected_hours = jhb_response["schedule"]["days"][0]["stages"][stage - 1]
except:
    dbn_affected_hours = []
    jhb_affected_hours = []
    
try:    
    cpt_stage = int(cpt_response["events"][0]["note"][6])
    if cpt_stage == 0: cpt_stage +=1
    cpt_affected_hours = cpt_response["schedule"]["days"][0]["stages"][cpt_stage - 1]
except:
    cpt_affected_hours = []
    


def all_affected_hours(campus):
    """Return all affected hours between 8am and 4pm"""
    all_hours = []
    
    try:
    
        if campus == "Durban":
            affected_hours = dbn_affected_hours
        elif campus == "Cape Town":
            affected_hours = cpt_affected_hours
        elif campus == "Johannesburg":
            affected_hours = jhb_affected_hours
            
        for n in affected_hours:
            if 8 <= int(n[0:2]) <= 16:
                all_hours.append(n)

        return all_hours
    except:
        return "Couldn't retrieve data."



if __name__ == "__main__":
    
    print(jhb_affected_hours)
    print(all_affected_hours("Durban"))    
