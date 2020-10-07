from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k < len(nums):
            temp = []
            for i in range(-k , 0):
                temp.append(nums[i])
                nums.pop(i)
            

            nums[:] = temp + nums
        print('hi')

sol = Solution()
a = sol.rotate([1,2], 3)
print(a)      