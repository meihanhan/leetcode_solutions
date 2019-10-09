import collections
def intersect(nums1, nums2):
    c1 = collections.Counter(nums1)
    c2 = collections.Counter(nums2)
    res = []
    for i in c1:
        if i in c2:
            for x in range(min(c1[i], c2[i])):
                res.append(i)
    return res     