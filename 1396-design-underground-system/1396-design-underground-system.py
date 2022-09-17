class UndergroundSystem:

    def __init__(self):
        self.visitors = {} # id: [station, time]
        self.trips = {} # City1City2 : [time, freq]
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.visitors[id] = [stationName, t]
        
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.visitors[id][1]
        trip = self.visitors[id][0] + "->" + stationName
        
        if trip in self.trips:
            tmp = self.trips[trip][0] * self.trips[trip][1]
            newVal = tmp + time 
            newVal /= self.trips[trip][1] + 1 
            self.trips[trip][0] = newVal
            self.trips[trip][1] += 1 
            
        else:
            self.trips[trip] = [time, 1] 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        concat = startStation + "->" + endStation
        return self.trips[concat][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)