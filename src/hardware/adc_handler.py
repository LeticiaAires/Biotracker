import smbus2
import time

class DFR0553:
    def __init__(self, bus_number=1, address=0x48):
        self.bus = smbus2.SMBus(bus_number)
        self.address = address

    def read_channel(self, channel):
        """
        Reads ADC value from the specified channel.
        :param channel: Channel number (0-3)
        :return: ADC value (0-1023)
        """
        if channel < 0 or channel > 3:
            raise ValueError("Channel must be between 0 and 3")
        self.bus.write_byte(self.address, channel)
        time.sleep(0.1)  # Allow ADC to settle
        return self.bus.read_byte(self.address)

    def close(self):
        self.bus.close()
