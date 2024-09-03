import time
import bluetooth
import pynput
from pyobd2 import OBD2

def find_obd2_devices():
    obd2_devices = []
    for device in bluetooth.discover_devices():
        if "OBD2" in device or "ELM327" in device:
            obd2_devices.append(device)

    return obd2_devices

def connect_to_obd2_device(device_address):
    obd2 = OBD2()
    obd2.connect_bluetooth(device_address)
    obd2.start_listening()
    obd2.set_baud_rate(115200)

    return obd2

def main():
    obd2_devices = find_obd2_devices()
    if len(obd2_devices) == 0:
        print("No OBD2 devices found")
        return

    print(f"OBD2 devices found: {obd2_devices}")

    # Assuming the first device is the target for simplicity
    device_address = obd2_devices[0]
    print(f"Connecting to OBD2 device: {device_address}")
    
    # Connect to the OBD2 device
    obd2 = connect_to_obd2_device(device_address)
    print("Connected to OBD2 device.")

    try:
        while True:
            # Here you can add the code to read data from the OBD2 device
            # For example, you can read vehicle speed
            speed = obd2.get_speed()
            print(f"Vehicle Speed: {speed} km/h")

            # Add a delay to avoid flooding the output
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        obd2.disconnect()
        print("Disconnected from OBD2 device.")

if __name__ == '__main__':
    main()
