from analysis import TemperatureAnalysis

def test_average():
    """Input file is a sine wave over 3 periods, average should be close to zero"""
    temperature_analysis = TemperatureAnalysis('weather_data.json', 'temperature_newyorkcity')
    assert abs(temperature_analysis.average()) < 1e-10


def test_std():
    """Input file is a sine wave with amplitude 5, standard deviation should be A/sqrt(2) = 3.5355"""
    temperature_analysis = TemperatureAnalysis('weather_data.json', 'temperature_newyorkcity')
    assert abs(temperature_analysis.std() - 3.5355) < 1e-4