import address_reader as ar
import address_writer as aw


URL = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'

headers = { 
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }

file = './input_data.csv'
data = ar.AddressReader(file, URL, headers).gen_data()
header = ['Company', 'Street', 'City', 'St', 'ZIPCode', 'Valid_Address']

aw.AddressWriter(file, data, header).csv_writer()


            
