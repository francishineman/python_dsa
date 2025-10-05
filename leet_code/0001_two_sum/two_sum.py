class Solution:

    def twoSum(nums, target):
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if target == n + m:
                    return(n,m)
                    break

# num_list = [3,6,1,2,7,8,4,5,9]
# target = 17
        
