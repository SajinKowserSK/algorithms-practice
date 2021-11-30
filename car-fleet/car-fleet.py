class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [] 
        cars = sorted([(x,y) for x, y in zip(position, speed)], reverse=True)
        for pos, speed in cars:        
            iterations = target - pos 
            iterations = iterations / speed 
            
            # print(pos, fleets)
            if len(fleets) == 0 or iterations > fleets[-1]:
                fleets.append(iterations)
                
        return len(fleets)