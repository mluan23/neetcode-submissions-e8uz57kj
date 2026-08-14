class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted non-decreasing (dupes allowed)
        # num 1 + num2 = target
        # oh so just 2sum
        # but 2 ptrs
        n = len(numbers)
        left = 0
        right = n-1
        # no binary serach because you need to look for 2 conditions essentially?

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left +1, right+1]
        return []