import time


class Solution:
    def isValid(self, s: str) -> bool:
        tmp_list=[]
        for i in range(len(s)):
            if(len(tmp_list)>0 and (  (s[i]==')' and tmp_list[-1]=='(')  or (s[i]==']' and tmp_list[-1]=='[') or (s[i]=='}' and tmp_list[-1]=='{') ) ):
                tmp_list.pop()
            else:
                tmp_list.append(s[i])
        if(tmp_list==[]):
            return True
        else:
            return False

if __name__ == '__main__':
    so = Solution()

    s="([)]"
    start = time.perf_counter()

    res = so.isValid(s)

    end = time.perf_counter()
    print("final is in ", end - start)
    print(res)
