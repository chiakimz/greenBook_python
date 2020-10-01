def removeDuplicates(nums) -> int:
    count = 1
    if nums == []:
        return 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1
    return count

li = removeDuplicates([1,1,2,3,3,3,4,4,5,6])
print("Hello")