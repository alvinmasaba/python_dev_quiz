# URL to which address data is posted
URL = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'

# Headers necessary to stop url from redirecting during POST
HEADERS = { 
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
      }

# I/O file name
FILE = './input_data.csv'

# Input file headings
HEADER = "Company,Street,City,St,ZIPCode,Address_Status\n"

    
