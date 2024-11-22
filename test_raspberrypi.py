import os
import psutil
import platform
import socket
import subprocess
import sys

def test_cpu():
    print("Testing CPU...")
    print(f"CPU Model: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical CPUs: {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")
    print()

def test_memory():
    print("Testing Memory...")
    memory = psutil.virtual_memory()
    print(f"Total RAM: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")
    print()

def test_disk():
    print("Testing Disk...")
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")
    print()

def test_resolution():
    print("Testing Screen Resolution...")
    try:
        # Querying screen resolution using xrandr command
        result = subprocess.check_output("xrandr | grep '*' | awk '{print $1}'", shell=True)
        resolution = result.decode("utf-8").strip()
        print(f"Screen Resolution: {resolution}")
    except Exception as e:
        print(f"Error getting screen resolution: {e}")
    print()

def test_network():
    print("Testing Network...")
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
        print("Checking internet connectivity...")
        response = os.system("ping -c 1 google.com")
        if response == 0:
            print("Internet is connected")
        else:
            print("No internet connection")
    except Exception as e:
        print(f"Error testing network: {e}")
    print()

def main():
    print("Starting Raspberry Pi Test...\n")
    
    test_cpu()
    test_memory()
    test_disk()
    test_resolution()
    test_network()

    print("Test Completed.")

if __name__ == "__main__":
    main()
