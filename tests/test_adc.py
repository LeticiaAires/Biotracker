from src.hardware.adc_handler import DFR0553

adc = DFR0553()
try:
    for i in range(4):
        value = adc.read_channel(i)
        print(f"Channel {i}: {value}")
finally:
    adc.close()
