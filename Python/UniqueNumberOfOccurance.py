def uniqueOccurrences(arr):
    nums = {}
    for i in arr:
        if i not in nums.keys():
            nums.update({i : 1})
        else:
            nums[i] += 1
    print(nums)
    values = list(nums.values())
    strs = [str(i) for i in values]
    len1 = len(strs)
    setStrings = set(strs)
    print(strs)
    print(setStrings)
    if len1 == len(setStrings):
        return True
    return False

uniqueOccurrences([1,2])