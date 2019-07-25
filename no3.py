class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_list=[]
        s_list=list(s)
        for i in range(len(s_list)):
            item_s=s_list[i]
            for j in range(i+1,len(s_list)):
                ss=s_list[j]
                b=item_s.find(s_list[j])
                if(item_s.find(s_list[j])>=0):
                    break
                item_s=item_s+s_list[j]
            tmp_list.append(item_s)
        length_list=[0]
        for i in tmp_list:
            length_list.append(len(i))
        length_max=max(length_list)
        #length_max_index=length_list.index(length_max)
        return length_max

if __name__=='__main__':
    so=Solution()
    s="abcabcbb"
    res=so.lengthOfLongestSubstring(s)
    print(res)