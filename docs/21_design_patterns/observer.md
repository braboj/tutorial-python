# observer

```python
# Example: Observer Pattern

# Subject Interface (produces data)
class Publisher(object):

    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


# Concrete Subject
class WeatherData(Publisher):

    def __init__(self):
        self.subscribers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.temperature, self.humidity, self.pressure)

    def set(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()


# Observer interface (consumes data)
class Subscriber(object):

    def update(self, temperature, humidity, pressure):
        pass


# Concrete Observer
class DisplayDevice(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(
            f"{self.name} Display - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")


# Client code
if __name__ == "__main__":

    # Create a weather station
    weather_station = WeatherData()

    # Attach a display device to the weather station
    display1 = DisplayDevice("Display 1")
    weather_station.attach(display1)

    # Attach another display device to the weather station
    display2 = DisplayDevice("Display 2")
    weather_station.attach(display2)

    # Simulate changes in weather data
    weather_station.set(25.0, 60.0, 1013.0)
    weather_station.set(26.5, 55.0, 1010.5)
```
