class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if not position or speed:
        #     return 0
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        times = []
        curr_max = 0
        # for i in range(len(cars)):
        #     times[i] = (target - cars[i][0]) // cars[i][1]
        for pos, spd in cars:
            times.append((target - pos)/spd)
        count = 0
        for i in range(len(times)):
            
            if times[i] > curr_max:
                count += 1
            curr_max = max(curr_max, times[i])
        return count
        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        # [1, 1, 7, 3, 12]
        [(4, 1), (2, 3), (0, 2)]
        [6, 2.66, 5]