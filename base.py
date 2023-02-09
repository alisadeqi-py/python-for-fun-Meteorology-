from abc import abstractmethod,ABC

class WeatherApi(ABC):
    def __init__(self,latitude,longitude):
        pass
    
    @abstractmethod
    def current_temprature():
        pass
