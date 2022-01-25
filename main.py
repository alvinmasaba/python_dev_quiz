from address_scraper import constants as cons, address_reader as ar, address_writer as aw

def main():
    # Post input file data to url, receive a response and return a list of formatted data
    data = ar.AddressReader(cons.FILE, cons.URL, cons.HEADERS).format_data()

    # Write the formatted data to the file, which will include the updated heading and subsequent values
    aw.AddressWriter(cons.FILE, data, cons.HEADER).csv_writer()


if __name__ == "__main__":
    print("Checking for valid addresses...")


main()