class Solution:
    # from leetcode problem "Burst balloons"
    def maxCoins(self, nums: List[int]) -> int:
        # added 1 and 1 to start and end of the array to drop adiitional cycle 
        nums = [1] + [n for n in nums] + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for temp_len in range(1, len(nums) - 1): # vary len of array
            for left in range(0, len(nums) - temp_len - 1): #vary left
                right = left + temp_len + 1 # calc right
                for mid in range(left + 1, right): # mid between left and right
                    '''calc max number of points from the part of the array from left to right 
                    consisting of temp_len elements moving mid which means that all ballons between left and mid 
                    and from mid to right have been already burnt'''
                    dp[left][right] = max(dp[left][right], 
                                          dp[left][mid] + dp[mid][right] + 
                                          nums[left]*nums[mid]*nums[right]
                                         )
        # return value from full array
        return dp[0][-1]   
