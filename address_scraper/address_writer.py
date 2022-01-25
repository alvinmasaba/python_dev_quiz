# class for writing to a csv file

class AddressWriter:
    def __init__(self, file, data, header):
        self.data = data
        self.file = file
        self.header = header

    def csv_writer(self):
        file = open(self.file, mode = 'w', encoding='utf-8')

        #write the header
        file.write(self.header)

        #write each line from data to the output file, excluding the header
        for row in self.data[1:]:
            file.write(f"{row['companyName']},{row['address1']},{row['city']},{row['state']},{row['zip']},{row['resultStatus']}\n")
        
        file.close()
