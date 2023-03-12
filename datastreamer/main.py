#! /usr/bin/python

from data_streamer.DataStreamer import DataStreamer
data_streamer = DataStreamer()

def main():
    counter = 0
    while True:
        # process incoming data from Excel/Data Streamer
        data_streamer_data = data_streamer.read_data()

        data_string = str(counter)
        if(counter==1000):
            counter = 0
        else:
            counter += 1

        if not data_streamer_data == None:
            for data in data_streamer_data:
                data_string += ","
                data_string += str(data)

        data_streamer.send_data(data_string)

if __name__ == '__main__':
    main()

