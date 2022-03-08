from typing import List
from numpy import arange, array
import numpy as np

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            p = nums.pop()
            nums.insert(0,p)
    
k = 3
nums = [1,5,7,9,11]
for i in range(k):
    p = nums.pop()
    nums.insert(0,p)
k = 3

length = len(nums)
arr = np.array(nums)

print(arr)
# for i in arange(length) :
#     if(i-1 < 0) :
#         t = length-1
#     else :
#         t = i -1
#     arr.add = nums[t]
    
# print(arr)

