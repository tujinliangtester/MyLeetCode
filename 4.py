

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        tmp_list = nums1 + nums2
        tmp_list.sort()

        if (len(tmp_list) % 2 == 0):
            i = len(tmp_list) / 2
            res = tmp_list[i - 1] + tmp_list[i]
            res = res / 2
        else:
            i = int((len(tmp_list) - 1) / 2)
            res = tmp_list[i]
        return res

if __name__=='__main__':
    so=Solution()
    nums1=[1,3]
    nums2=[2]
    res=so.findMedianSortedArrays(nums1,nums2)
    print(res)