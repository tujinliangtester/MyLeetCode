class Solution:
    def reverse(self, x: int) -> int:
        tmp_list=[]
        position_val=position_key=0
        flag=1
        if(x<0):
            flag=-1
            x=0-x
        while(True):
            tmp_x=int(x/10)
            tmp_val=x%10
            x=tmp_x
            tmp_list.append(tmp_val)
            if(tmp_x==0):break
        tmp_y=0
        for (i,val) in enumerate(tmp_list):
            tmp_y+=10**(len(tmp_list)-i-1)*tmp_list[i]
        if (tmp_y > (2 ** 31 - 1)):
            tmp_y = 0
        if(flag<0 and tmp_y>0):
            tmp_y=0-tmp_y
        return tmp_y


if __name__ == '__main__':
    so=Solution()
    x=1534236469
    y=so.reverse(x)
    print(y)