def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    if n2 > n1:
        return findMedianSortedArrays(nums2, nums1)
    low, hi = 0, n2
    half1 = ((n1 + n2 + 1) // 2)
    while low <= hi:
        mid2 = (low + hi) // 2
        mid1 = half1 - mid2

        l1 = float("-inf") if not mid1 else nums1[(mid1-1)]
        l2 = float("-inf") if not mid2 else nums2[(mid2-1)]
        r1 = float("inf") if mid1 == n1 else nums1[mid1]
        r2 = float("inf") if mid2 == n2 else nums2[mid2]

        if (l1 > r2): 
            low = mid2 + 1
        elif (l2 > r1):
            hi = mid2 - 1
        else: 
            if (n1+n2) % 2 == 0:
                return (max(l1,l2) + min(r1, r2)) / 2
            return max(l1, l2)
    return -1
