class UndergroundSystem:

    def __init__(self):
        self.trips ={}
        self.checkins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        key = (startStation,stationName)
        duration = t - startTime
        if key in self.trips:
            self.trips[key].append(duration)
        else:
            self.trips[key] = [duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation,endStation)
        return sum(self.trips[key]) / len(self.trips[key])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
