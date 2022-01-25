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

        #write each line from data
        for line in self.data[1:]:
            file.write(f"{line['companyName']},{line['address1']},{line['city']},{line['state']},{line['zip']},{line['resultStatus']}\n")
        
        file.close()
