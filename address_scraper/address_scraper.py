from termios import CKILL
import requests
import csv, json 

URL = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'

with open('./input_data.csv', 'rb') as csvfile:
    address_reader = csv.DictReader(csvfile, fieldnames= ('companyName', 'address1', 'city', 
    'state', 'zip'))
    
    headers = { 
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
       'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

    header = True
    for payload in address_reader:
        if header:
            next
            header = False
        else:
            r = requests.post(URL, data=payload, headers=headers)
            
            if r["resultStatus"] == 'SUCCESS':
              print(payload["companyName"])
                
            
