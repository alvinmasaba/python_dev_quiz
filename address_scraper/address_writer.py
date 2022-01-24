import csv

# class for writing to a csv file
class AddressWriter:
    def __init__(self, file, data, header):
        self.data = data
        self.file = file
        self.header = header

    def csv_writer(self):
        with open('./input_data.csv', mode = 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            #write the header
            writer.writerow(self.header)

            #for each item in data, write the desired values to the row, excluding the header
            for line in self.data[1:]:
                writer.writerow([line['companyName'], line['address1'], line['city'], line['state'], line['zip'], line['resultStatus']])
