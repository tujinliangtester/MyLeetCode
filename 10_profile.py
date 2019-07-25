
import profile

def isMatch(s: str, p: str, k=0) -> bool:
    length_s = len(s)
    length_p = len(p)

    # 不用每次都来进行对p的操作
    if (k == 0):
        # 连续多个星号的情况完善
        i = 0
        while (True):
            if (i >= len(p)): break
            if (i + 1 < len(p)):
                if (p[i] == p[i + 1] == '*'):
                    p = p[:i] + p[i + 1:]
            i += 1

        #  效率优化，先去掉重复的
        tmp_list_i = []
        i = 0
        while (True):
            if (i >= len(p)): break
            if (i + 3 < len(p)):
                if (p[i] != '*'):
                    if (p[i + 1] == '*'):
                        if (p[i + 2] == p[i]):
                            if (p[i + 3] == '*'):
                                tmp_list_i.append(i)
                                i += 1
            i += 1
        for i in range(len(tmp_list_i)):
            j = len(tmp_list_i) - 1 - i
            m = tmp_list_i[j]
            p = p[:m] + p[m + 2:]

    def calStrCharRepeatNum(cal_str, cal_index):
        cal_num = 1
        for i in range(cal_index, len(cal_str) - 1):
            if (cal_str[i] == cal_str[i + 1]):
                cal_num += 1
            else:
                break
        return cal_num

    for i in range(k, length_p):
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
                    s_char_repeat_num = calStrCharRepeatNum(s, i - 1)

                # 注意，这里的s_char_repeat_num+1是因为前闭后开
                for times in range(0, s_char_repeat_num + 1):
                    tmp_p = p[:i - 1]
                    for in_times in range(times):
                        tmp_p = tmp_p + charBeforStar
                    tmp_p = tmp_p + p[i + 1:]
                    isMatchFlag_times = isMatch(s, tmp_p, i + times)
                    if (isMatchFlag_times == True):
                        return True

    if (length_s != length_p):
        return False
    for index_i in range(length_s):
        if (p[index_i] == '.' or s[index_i] == p[index_i]):
            continue
        else:
            return False
    return True


if __name__ == '__main__':

    profile.run("isMatch('bbaabcbaaccbaaaa','a*c*ba*.b.*b.*c*.*c')")