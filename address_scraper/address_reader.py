import requests

# class for posting data from csv rows to a url and compiling each response as a list item
class AddressReader:
    def __init__(self, file, url, headers):
        self.data = []
        self.file = file
        self.url = url
        self.headers = headers

    def fetch_response(self, post_data):
        r = requests.post(self.url, data=post_data, headers=self.headers).json()
        post_data['resultStatus'] = r['resultStatus'] 
        
        if  post_data['resultStatus'] == "SUCCESS":
            post_data['resultStatus'] = "VALID"

        return post_data

    def csv_parser(self):
        file = open(self.file, mode = 'r', encoding='utf-8')

        for line in file:
            values = line.split(',')
            payload = { 'companyName': values[0], 'address1': values[1], 'city': values[2], 
            'state': values[3], 'zip': values[4].strip('\n'), }
            payload = self.fetch_response(payload)
            self.data.append(payload)

        file.close()

        return self.data

    


  
