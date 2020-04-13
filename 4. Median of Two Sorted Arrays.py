def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    if n2 > n1:
        return findMedianSortedArrays(nums2, nums1)
    low, hi = 0, n2
    half1 = ((n1 + n2 + 1) // 2)
    while low <= hi:
        partition2 = (low + hi) // 2
        partition1 = half1 - mid2

        l1 = float("-inf") if not partition1 else nums1[partition1 - 1]
        l2 = float("-inf") if not partition2 else nums2[partition2 - 1]
        r1 = float("inf") if partition1 == n1 else nums1[partition1]
        r2 = float("inf") if partition2 == n2 else nums2[partition2]

        if (l1 > r2): 
            low = partition2 + 1
        elif (l2 > r1):
            hi = partition2 - 1
        else: 
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            return max(l1, l2)
    return -1
