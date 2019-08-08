class Solution:
    def romanToInt(self, s: str) -> int:
        int_tmp=0
        i=-1
        while(True):
            i+=1
            if(i>len(s)-1):break
            if(s[i]=='I'):
                if(i+1<len(s) ):
                    if(s[i+1]=='V'):
                        int_tmp+=4
                        i+=1
                    elif(s[i+1]=='X'):
                        int_tmp+=9
                        i+=1
                    else:
                        int_tmp += 1

                else:
                    int_tmp += 1
            elif (s[i] == 'X'):
                if (i + 1 < len(s)):
                    if (s[i + 1] == 'L'):
                        int_tmp += 40
                        i+=1

                    elif (s[i + 1] == 'C'):
                        int_tmp += 90
                        i+=1
                    else:
                        int_tmp += 10

                else:
                    int_tmp += 10
            elif (s[i] == 'C'):
                if (i + 1 < len(s)):
                    if (s[i + 1] == 'D'):
                        int_tmp += 400
                        i+=1

                    elif (s[i + 1] == 'M'):
                        int_tmp += 900
                        i+=1
                    else:
                        int_tmp += 100

                else:
                    int_tmp += 100
            elif (s[i] == 'V'):
                int_tmp += 5
            elif(s[i] == 'L'):
                int_tmp += 50
            elif (s[i] == 'D'):
                int_tmp += 500
            elif (s[i] == 'M'):
                int_tmp += 1000
        return int_tmp

if __name__ == '__main__':
    so = Solution()
    s='MCMXCIV'
    res=so.romanToInt(s)
    print(res)

