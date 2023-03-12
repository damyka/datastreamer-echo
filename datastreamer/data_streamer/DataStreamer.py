from time import process_time
import serial

class DataStreamer:
    def __init__(self):
        self.serial_data_array = [0]
        self.serial = serial.Serial(
            port='/dev/ttyS0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def send_data(self, data):
        data = self.__process_data(data)
        self.serial.write(data.encode('utf-8'))

    def __process_data(self, data):
        if not isinstance(data, str):
            data = str(data)
        if not data.endswith("\n"):
            data += "\n"
        return data

    def send_data_array(self, data_array):
        data_string = self.__process_data_array(data_array)
        self.send_data(data_string)

    def __process_data_array(self, data_array):
        data_string = ""
        for data in data_array:
            data_string += str(data)
            data_string += ","
        return data_string

    def read_data(self):
        data = self.serial.readline().decode()
        if data == "":
            return None
        if data != "":
            self.serial_data_array = data.split(",")
        else:
            self.serial_data_array[0] = data
        return self.serial_data_array