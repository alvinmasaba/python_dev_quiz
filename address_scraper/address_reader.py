import requests


class AddressReader:
    def __init__(self, file, url, headers):
        self.data = []
        self.file = file
        self.url = url
        self.headers = headers

    def format_data(self):
        csv_file = open(self.file, mode = 'r', encoding='utf-8')

        for row in csv_file:
            # format data into a dictionary
            payload = self.csv_parser(row)
            # post data to url and return the properly formatted response
            data = self.fetch_response(payload)
            # append the response to list
            self.data.append(data)
            
        csv_file.close()

        return self.data

    def csv_parser(self, row):
        # Parses the input string to a dict with keys matching the urls required post headings
        values = row.split(',')
        payload = { 'companyName': values[0], 'address1': values[1], 'city': values[2], 
        'state': values[3], 'zip': values[4].strip('\n'), 
        }
         
        return payload

    def fetch_response(self, post_data):
        r = requests.post(self.url, data=post_data, headers=self.headers).json()

        # adds resultStatus and its response value to the output data 
        post_data['resultStatus'] = r['resultStatus'] 
        
        # our output file will denote valid addresses as 'VALID'
        if  post_data['resultStatus'] == "SUCCESS":
            post_data['resultStatus'] = "VALID"

        return post_data 
