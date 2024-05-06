'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

def findMedianSortedArrays(nums1, nums2):
    mergedNums=nums1+nums2
    mergedNums.sort()
    lengthNums=len(mergedNums)
    if lengthNums%2==1:
        median=round(lengthNums/2)
        return float(mergedNums[median-1])
    else:
        median=int((lengthNums/2)-1)
        return (mergedNums[median]+mergedNums[median+1])/2

print(findMedianSortedArrays([1,2],[3,4]))