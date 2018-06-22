class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = False
        in_flag = False
        if len(nums)<=1: pass
        elif nums[-1]>nums[-2]:
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
            
        else:
            for i in range(len(nums)-2,-1,-1):
                if i>0 and nums[i]>nums[i-1] and nums[i]>=nums[i+1]:
                    ind = i-1
                    for j in range(i+1,len(nums)):
                        if nums[ind]>=nums[j]:
                            temp = nums[j-1]
                            nums[j-1] = nums[ind]
                            nums[ind] = temp
                            l,r = ind+1, len(nums)-1
                            while l<r:
                                temp = nums[l]
                                nums[l] = nums[r]
                                nums[r] = temp
                                l+=1
                                r-=1
                            in_flag = True
                            break
                    if in_flag == False:
                        temp = nums[-1]
                        nums[-1] = nums[ind]
                        nums[ind] = temp
                        l,r = ind+1, len(nums)-1
                        while l<r:
                            temp = nums[l]
                            nums[l] = nums[r]
                            nums[r] = temp
                            l+=1
                            r-=1
                        
                    flag = True
                elif i==0 and nums[i]>=nums[i+1] and flag==False:
                    flag = True
                    nums.reverse()
                if flag: break
  
  
  ### Use sorted() instead of .sort()
