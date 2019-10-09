def singleNumber(nums):
    notDuplicateNums = []
    for i in nums:
        if i in notDuplicateNums:
            notDuplicateNums.remove(i)
        else:
            notDuplicateNums.append(i)
    return notDuplicateNums[0]

singleNumber([1,0,1])