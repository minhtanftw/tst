import pyvisa
import time

#Connect to oscilloscope

rm = pyvisa.ResourceManager()

scope = rm.open_resource("USB0::0x0699::0x0363::C102220::INSTR")

#Configure and measure

scope.write(":AUTOSCALE")

time.sleep(1)
waveform = scope.query(":MEASure:VAVerage?")

print(f"Average voltage = {waveform}")