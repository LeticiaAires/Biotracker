# Biotracker

# Compost Monitoring System with Raspberry Pi and Environmental Sensors

This project aims to track key environmental parameters in a composting system using a Raspberry Pi and various sensors. The goal is to monitor and evaluate the composting process, comparing real-time data with a reference database to determine whether the compost is progressing as expected. Based on the analysis, the system will provide suggestions (e.g., add more water or nitrogen) to help optimize the composting conditions.

## Sensors Used:
- **pH sensor**: Measures the acidity or alkalinity of the compost.
- **CO2 sensor**: Measures carbon dioxide levels, an indicator of microbial activity.
- **Methane sensor**: Detects methane, which is a byproduct of anaerobic decomposition.
- **Temperature sensor**: Monitors the temperature to ensure the compost stays within the optimal range for microbial activity.
- **Moisture sensor**: Measures the moisture content, ensuring the compost has the right level of humidity for optimal decomposition.

## Project Objective
This system is designed to provide continuous monitoring of a compost heap, helping the user evaluate the composting process in real-time. It compares the sensor readings with a predefined set of ideal conditions (based on a database) and provides recommendations on how to improve the composting process. For example, it could suggest adding more water if the moisture levels are too low or adjusting the nitrogen content if needed.

## Features:
- Real-time monitoring of pH, CO2, methane, temperature, and moisture levels.
- Database comparison to track whether the composting process is within optimal parameters.
- Actionable suggestions based on sensor data, such as adjusting moisture levels or nitrogen.
- Easy-to-read graphical interface for visualizing the composting environment.

## Hardware Requirements:
- **Raspberry Pi 4 (or 5)**: The main controller for managing the sensors and processing the data.
- **pH sensor**: To measure the acidity or alkalinity of the compost.
- **CO2 sensor**: To monitor the CO2 concentration in the compost environment.
- **Methane sensor**: To detect methane gas levels.
- **Temperature sensor**: To measure the temperature of the compost.
- **Moisture sensor**: To check the moisture content of the compost.

## Software Requirements:
- **Raspberry Pi OS**: The operating system running on your Raspberry Pi.
- **Python 3**: For scripting and sensor integration.
- **psutil**: For system monitoring.
- **Database (e.g., SQLite, MySQL)**: For storing the ideal conditions of composting and comparing real-time data.
- **Matplotlib/Plotly** (optional): For graphical data visualization.
  
### Install Dependencies:
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/compost-monitoring.git
    cd compost-monitoring
    ```

2. **Install necessary Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Setup Instructions:
1. **Connect the Sensors**:
   - Connect each sensor (pH, CO2, methane, temperature, and moisture) to the Raspberry Pi following the wiring instructions for each sensor (refer to the sensor manuals for correct wiring).
   
2. **Configure the Database**:
   - You will need a database (e.g., SQLite) to store ideal composting parameters and sensor readings. Configure it according to your sensor specifications and ideal compost parameters.
   
3. **Configure Python Script**:
   - Modify the configuration files (if needed) to reflect your sensor GPIO pin connections and database settings.

4. **Run the System**:
   - After setting up the sensors and database, run the monitoring system using the following command:

   ```bash
   python3 compost_monitoring.py
