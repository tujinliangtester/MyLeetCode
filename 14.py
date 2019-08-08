class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = -1
        res = ''
        if(len(strs)==0):return res
        if(len(strs[0])==0):return res
        res_tmp = strs[0][0]

        while (True):
            i += 1
            if (i >= len(strs[0])): break
            if (i > 0):
                res_tmp = strs[0][:i+1]
            f = True
            for item in strs:
                if (item.find(res_tmp) != 0):
                    f = False
                    break
            if (f == True):
                res = res_tmp
        return res


if __name__ == '__main__':
    so = Solution()
    s = ["aa","aa"]
    res = so.longestCommonPrefix(s)
    print(res)
