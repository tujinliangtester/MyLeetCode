import time
import profile
class Solution:
    def isMatch_2(self, s: str, p: str) -> bool:
        i = 0
        flag = False
        out_flag = False
        while (True):
            if (flag == True): break
            if (out_flag == True): break
            if (p == ''): return False
            if (p[0] != s[0] and p[0] != '.' or p[0] == '*'):
                p = p[1:]
                continue
            j = 0
            for i in range(len(s)):
                tmp_char = p[j]
                if (tmp_char == '.'):
                    j += 1
                    continue
                if (tmp_char == '*'):
                    tmp_char = p[j - 1]
                    if (tmp_char != s[i]):
                        j += 1
                        p = p[j:]
                        j = 0
                    else:
                        j += 1

                else:
                    if (tmp_char != s[i]):
                        j += 1
                        p = p[j:]
                        j = 0
                    else:
                        j += 1
                if (j > (len(p) - 1) and i == len(s) - 1):
                    flag = True
                    break
                if (j > (len(p) - 1) and i < len(s) - 1):
                    out_flag = True
                    break
        return flag

    # 主要通过区分*来进行判定
    def isMatch_3(self, s: str, p: str) -> bool:
        j = 0
        i = -1
        isMathFlag = True
        while (True):
            if (isMathFlag == False):
                break
            i += 1
            if (i < len(s)):
                if (j >= len(p)):
                    isMathFlag = False
                    break
                if (p[j] == '*'):
                    j += 1
                    if (j < len(p)):
                        p = p[j:]
                        j = 0
                    else:
                        isMathFlag = False
                    i -= 1
                elif (j + 1 < len(p) and p[j + 1] == '*'):
                    starCharMatchFlag = False
                    while (True):
                        if (i >= len(s)):
                            break
                        if (p[j] != s[i] and p[j] != '.'):
                            if (starCharMatchFlag == False):
                                j += 2
                                if (j < len(p)):
                                    i -= 1
                                    break
                                else:
                                    isMathFlag = False
                                    break
                            else:
                                j += 2
                                i -= 1
                                break
                        else:
                            starCharMatchFlag = True
                            i += 1
                else:
                    if (p[j] != s[i] and p[j] != '.'):
                        isMathFlag = False
                    else:
                        j += 1
            else:
                if (j >= len(p)):
                    break
                if (p[j] == '*'):
                    j += 1
                    i -= 1
                elif (j - 2 >= 0 and len(s) > 0 and p[j - 2] == s[-1] and p[j - 1] == '*' and p[j] == s[-1]):
                    j += 1
                    i -= 1
                elif (j + 1 < len(p) and p[j + 1] == '*'):
                    j += 2
                    i -= 1
                else:
                    isMathFlag = False
        return isMathFlag

    # 重新理逻辑，让*带着字符循环匹配，如果出现不匹配，则直接退出，或者匹配满对应s中的字母数量
    def isMatch(self, s: str, p: str,k=0) -> bool:

        length_s=len(s)

        # 不用每次都来进行对p的操作
        if(k==0):
            # 连续多个星号的情况完善
            i = 0
            while (True):
                if (i >= len(p)): break
                if (i + 1 < len(p)):
                    if (p[i] == p[i + 1] == '*'):
                        p = p[:i] + p[i + 1:]
                i += 1

            #  效率优化，先去掉重复的
            tmp_list_i=[]
            i=0
            while(True):
                if(i>=len(p)):break
                if(i+3<len(p)):
                    if(p[i] !='*'):
                        if( p[i+1]=='*'):
                            if( p[i+2]==p[i]):
                                if( p[i+3]=='*'):
                                    tmp_list_i.append(i)
                                    i+=1
                i+=1
            for i in range(len(tmp_list_i)):
                j=len(tmp_list_i)-1-i
                m=tmp_list_i[j]
                p=p[:m]+p[m+2:]

        def calStrCharRepeatNum(cal_str,cal_index):
            cal_num=1
            for i in range(cal_index,len(cal_str)-1):
                if(cal_str[i]==cal_str[i+1]):
                    cal_num+=1
                else:
                    break
            return cal_num


        for i in range(k,len(p)):
            if (p[i] == '*'):
                if (i == 0):
                    break
                else:
                    charBeforStar = p[i - 1]

                    # 经过试验  发现不能对s进行处理，那么就需要转换一下思路，用s中对应字符重复的次数来作为p中*叠加次数的上限
                    # 如果*符号前是.符号，则长度最长可以是s余下的所有字符长度
                    if (p[i - 1] == '.'):
                        s_char_repeat_num = length_s - i + 1
                    else:
                        # 注意，这里的i-1的意思，是指跟p一样的字母的索引，而不是i（此时i对应的是*符号）
                        s_char_repeat_num=calStrCharRepeatNum(s,i-1)

                    #注意，这里的s_char_repeat_num+1是因为前闭后开
                    for times in range(0, s_char_repeat_num+1):
                        tmp_p = p[:i - 1]
                        for in_times in range(times):
                            tmp_p = tmp_p+charBeforStar
                        tmp_p = tmp_p+p[i+1:]
                        isMatchFlag_times = self.isMatch(s, tmp_p,i+times)
                        if (isMatchFlag_times == True):
                            return True


        if(length_s!=len(p)):
            return False
        for index_i in range(length_s):
            if(p[index_i]=='.' or s[index_i]==p[index_i]  ):
                continue
            else:
                return False
        return True

    # 重大调整，将n次转换成0次和1次，即同时先对s和p进行简化  经测试  是失败的  错误的
    def isMatch_4(self, s: str, p: str,k=0) -> bool:
        # p中没有星号，则直接匹配
        hasStar=False
        for i in range(len(p)):
            if(p[i]=='*' and i>=1):
                hasStar=True
                break

        if(hasStar==False):
            if (s == p):
                return True
            if (len(s) != len(p)):
                return False
            else:
                for inner_i in range(len(s)):
                    if (s[inner_i] != p[inner_i] and p[inner_i] != '.'):
                        return False
                return True


        # p连续多个星号的情况完善
        i = 0
        while (True):
            if (i >= len(p)): break
            if (i + 1 < len(p)):
                if (p[i] == p[i + 1] == '*'):
                    p = p[:i] + p[i + 1:]
                    i=-1
            i += 1

        #  p效率优化，先去掉重复的
        tmp_list_i=[]
        i=0
        while(True):
            if(i>=len(p)):break
            if(i+3<len(p)):
                if(p[i] !='*' and p[i+1]=='*' and p[i+2]==p[i] and p[i+3]=='*'):
                    tmp_list_i.append(i)
                    i+=1
            i+=1
        for i in range(len(tmp_list_i)):
            j=len(tmp_list_i)-1-i
            m=tmp_list_i[j]
            p=p[:m]+p[m+2:]

        # p的*符号前后字母一样时，直接将后一个字母去掉
        for i in range(len(p)):
            if(i+2<len(p)):
                if(p[i]==p[i+2] and p[i+1]=='*'):
                    if(i+3<len(p)):
                        p=p[:i+2]+p[i+3]
                    else:
                        p=p[:i+2]

        # todo  不能这样处理，因为这样会有问题，相当于不确定了连续字母的个数，而如果p中是确定的个数时，则会出现匹配不上的情况

        # s的连续字母简化
        i=0
        tmp_list_s=list(s)
        while(True):
            if(i>len(s)):
                break
            if(i+1<len(s)):
                if(s[i]==s[i+1]):
                    tmp_list_s[i+1]='*'
            i+=1
        s=''.join(tmp_list_s)
        # s连续多个星号的情况完善
        i = 0
        while (True):
            if (i >= len(s)): break
            if (i + 1 < len(s)):
                if (s[i] == s[i + 1] == '*'):
                    s = s[:i] + s[i + 1:]
                    i=-1
            i += 1

        #匹配逻辑
        for i in range(k,len(p)):
            if (p[i] == '*'):
                if (i == 0):
                    break
                else:
                    if(i-2==0):
                        tmp_p = p[0] + p[i+1:]
                    else:
                        tmp_p = p[:i - 1] + p[i+1:]
                    # *号匹配0次
                    isMatchFlag = self.isMatch(s, tmp_p,i)
                    if (isMatchFlag == False):
                        tmp_p = p
                        # *号匹配1次
                        isMatchFlag_times = self.isMatch(s, tmp_p,i+1)
                        if (isMatchFlag_times == True):
                            return True
                    else:
                        return True

        if (s == p):
            return True
        if (len(s) != len(p)):
            return False
        else:
            for inner_i in range(len(s)):
                if(inner_i-1>=0 and p[inner_i-1]=='.' and p[inner_i]=='*'):
                    continue
                if (inner_i - 1 >= 0 and s[inner_i - 1] == p[inner_i] and s[inner_i] == '*'):
                    continue
                if (s[inner_i] != p[inner_i] and p[inner_i] != '.'):
                    return False
        return True

if __name__ == '__main__':
    so = Solution()
    s = 'bcbacacbacbbbbcac'
    p = '..*a*a*b*c*.*a*bb*.'
    start = time.perf_counter()

    res = so.isMatch(s, p)
    end = time.perf_counter()
    print("final is in ", end - start)
    print(res)
    # profile.run("isMatch('bbaabcbaaccbaaaa','a*c*ba*.b.*b.*c*.*c')")
