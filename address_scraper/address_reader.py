import requests, json

# class for posting data from csv rows to a url and compiling each response as a list item
class AddressReader:
    def __init__(self, file, url, headers):
        self.data = []
        self.csv = {}
        self.file = file
        self.url = url
        self.headers = headers

    def parse(self):
        file = open(self.file, mode = 'r', encoding='utf-8')

        for line in file:
            values = line.split(',')
            payload = { 'companyName': values[0], 'address1': values[1], 'city': values[2], 
            'state': values[3], 'zip': values[4].strip('\n'), }
            r = requests.post(self.url, data=payload, headers=self.headers)
            result = json.loads(r.text)
            payload['resultStatus'] = result['resultStatus']
            self.data.append(payload)

        file.close()
        return self.data


    

  
