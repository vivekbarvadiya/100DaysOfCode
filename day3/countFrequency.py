class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1

        
        arr=[]
        for i in hash:
            arr.append(hash[i])
            print(arr)

        x=max(arr)
        y=arr.count(x)

        return x*y