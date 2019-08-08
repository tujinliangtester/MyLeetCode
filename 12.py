
class Solution:
    def intToRoman(self, num: int) -> str:
        i=0
        list_tmp=[]
        while(num>0):
            str_tmp=''
            i+=1
            n = num % 10
            num = int(num / 10)
            if(i==1):
                if(n==1):
                    str_tmp='I'
                elif(n==2):
                    str_tmp='II'
                elif (n == 3):
                    str_tmp = 'III'
                elif (n == 4):
                    str_tmp = 'IV'
                elif (n == 5):
                    str_tmp = 'V'
                elif (n == 6):
                    str_tmp = 'VI'
                elif (n == 7):
                    str_tmp = 'VII'
                elif (n == 8):
                    str_tmp = 'VIII'
                elif (n == 9):
                    str_tmp = 'IX'
            elif(i==2):
                if (n == 1):
                    str_tmp = 'X'
                elif (n == 2):
                    str_tmp = 'XX'
                elif (n == 3):
                    str_tmp = 'XXX'
                elif (n == 4):
                    str_tmp = 'XL'
                elif (n == 5):
                    str_tmp = 'L'
                elif (n == 6):
                    str_tmp = 'LX'
                elif (n == 7):
                    str_tmp = 'LXX'
                elif (n == 8):
                    str_tmp = 'LXXX'
                elif (n == 9):
                    str_tmp = 'XC'
            elif(i==3):
                if (n == 1):
                    str_tmp = 'C'
                elif (n == 2):
                    str_tmp = 'CC'
                elif (n == 3):
                    str_tmp = 'CCC'
                elif (n == 4):
                    str_tmp = 'CD'
                elif (n == 5):
                    str_tmp = 'D'
                elif (n == 6):
                    str_tmp = 'DC'
                elif (n == 7):
                    str_tmp = 'DCC'
                elif (n == 8):
                    str_tmp = 'DCCC'
                elif (n == 9):
                    str_tmp = 'CM'
            elif (i == 4):
                if (n == 1):
                    str_tmp = 'M'
                elif (n == 2):
                    str_tmp = 'MM'
                elif (n == 3):
                    str_tmp = 'MMM'
                else:
                    print('超出范围!!!')
                    break
            list_tmp.append(str_tmp)
        list_tmp.reverse()
        res=''.join(list_tmp)
        return res

if __name__ == '__main__':
    so = Solution()
    res=so.intToRoman(58)
    print(res)

