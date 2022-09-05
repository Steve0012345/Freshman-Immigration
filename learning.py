class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = "I"
        if (r == 'I'):
          return 1
        if (r == 'V'):
          return 5
        if (r == 'X'):
          return 10
        if (r == 'L'):
          return 50
        if (r == 'C'):
          return 100
        if (r == 'D'):
          return 500
        if (r == 'M'):
          return 1000
        return -1

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lled = ["h", "e", "l", "l", "o"]
        lled.reverse()
        print(lled)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target = 9
        nums = [2, 7, 11, 15]
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i+1] == target):
                return [i, i+1]
            return None