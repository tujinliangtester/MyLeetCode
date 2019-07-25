

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):return False
        tmp_list=[]
        y_tmp=x
        while(True) :
            tmp_val=x%10
            x=int(x/10)
            tmp_list.append(tmp_val)

            if(x==0):break
        y=0
        for (i,val) in enumerate(tmp_list):
            y+=val*10**(len(tmp_list)-i-1)
        if(y==y_tmp):
            return True
        return False




if __name__ == '__main__':
    so=Solution()
    res=so.isPalindrome(1221)
    print(res)