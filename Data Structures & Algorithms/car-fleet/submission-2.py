class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of number of steps, any that have the same steps are
        # going to be in same fleet
        mappings = dict()
        for i in range(len(position)):
            mappings[position[i]] = speed[i]
        position = sorted(position)

        steps = [0] * len(position)
        for i in range(len(position)):
            steps[i] = (target - position[i]) / mappings.get(position[i])
        num_fleets = 0
        curr_slowest = 0
        print(steps)
        for i in range(len(steps)-1, -1, -1):
            if steps[i] > curr_slowest:
                num_fleets += 1
                curr_slowest = steps[i]
        return num_fleets

