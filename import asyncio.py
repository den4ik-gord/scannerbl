import asyncio
from bleak import BleakScanner

 
async def reop():
    
    measured_power = -43
    N = 3
    while True:
        d = await BleakScanner.find_device_by_address("EE:97:75:4D:A0:79")
        if not d is None:
            dist = 10**((measured_power - d.rssi)/(10*N))
            print(d.name, d.address, d.rssi, dist)
