from pathlib import Path
import json
import numpy as np

class TemperatureAnalysis:
    """Class that wraps around time and temperature data and computes values"""

    def __init__(self, filename, temperature_key='temperature'):
        """
        Initialize and read in time and temperature data

        Args:
            filename (str): JSON file containing list of dictionaries with time and 
                      temperature data. By default looks for the keys 'time' and
                      'temperature'
            temperature_key: alternative key to use for temperature data
        """
        path = Path(filename)
        try:
            contents = path.read_text()
            data = json.loads(contents)
        except FileNotFoundError:
            print(f'The file {filename} does not exist.')
            data = None
        except json.JSONDecodeError:
            print(f'The file {filename} is corrupt.')
            data = None

        if data == None:
            self.times = None
            self.temperatures = None

        # Create lists of time and temperature data from list of dictionaries in JSON file
        self.times = np.zeros(len(data))
        self.temperatures = np.zeros(len(data))
        for i in range(len(data)):
            self.times[i] = data[i]['time']
            self.temperatures[i] = data[i][temperature_key]

    def average(self):
        """Calculate the average of the temperature data"""
        if self.temperatures is None:
            return None
        return np.average(self.temperatures)

    def std(self):
        """Calculate the standard deviation of the temperature data"""
        if self.temperatures is None:
            return None
        return np.std(self.temperatures)