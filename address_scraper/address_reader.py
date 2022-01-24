import csv, requests, json

# class for posting data from csv rows to a url and compiling each response as a list item
class AddressReader:
    def __init__(self, file, url, headers):
        self.data = []
        self.file = file
        self.url = url
        self.headers = headers

    def gen_data(self):
      with open(self.file, mode = 'r', encoding='utf-8') as csvfile:
          address_reader = csv.DictReader(csvfile, fieldnames= ('companyName', 'address1', 'city', 'state', 'zip'))

          for payload in address_reader:
              r = requests.post(self.url, data=payload, headers=self.headers)
              result = json.loads(r.text)
              payload['resultStatus'] = result['resultStatus']
              self.data.append(payload)

      return self.data

    

  
