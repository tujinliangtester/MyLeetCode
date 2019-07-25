class Solution:
    def convert(self, s: str, numRows: int) :
        length_s=len(s)
        col_list=[]
        for i in range(numRows):
            col_list.append(' ')
        sq_list = []
        down_direction = True
        index_s = 0
        up_row = numRows - 2
        while(index_s + 1 <= length_s):
            col_list_tmp=col_list[:]
            if (down_direction):
                for row in range(numRows):
                    if(index_s + 1 <= length_s):
                        col_list_tmp[row] = s[index_s]
                        index_s += 1
                    else:
                        break
                down_direction = False
            else:
                if(up_row>0):
                    col_list_tmp[up_row] = s[index_s]
                    index_s += 1
                    up_row-=1
                    if (up_row == 0):
                        down_direction = True
                        up_row = numRows - 2
                else:
                    down_direction=True
            sq_list.append(col_list_tmp)

        res_s=''
        for i in range(numRows):
            for j in range(len(sq_list)):
                tmp_s=sq_list[j][i]
                res_s+=tmp_s

        res_s=res_s.replace(' ','')
        return res_s
    def convert2(self, s: str, numRows: int) :
        #todo
        line_len=0
        sq_list=[]
        if(numRows==1):
            return s
        elif(numRows==2):
            i=0
            while(True):
                i+=1
                tmp_list=[]
                if(2*i<len(s)):
                    tmp_list.append(s[2*i])
                else:break
                if(2*i+1<len(s)):
                    tmp_list.append(s[2*i+1])
                sq_list.append(tmp_list)
            res_s = ''
            for i in range(numRows):
                for j in range(len(sq_list)):
                    tmp_s = sq_list[j][i]
                    res_s += tmp_s

            res_s = res_s.replace(' ', '')
            return res_s
        else:
            col_list = []
            for i in range(numRows):
                col_list.append(' ')

            line_len=numRows+numRows-2
            while (True):
                i = 0
                i += 1
                tmp_list = []
                if (line_len * i < len(s)):
                    tmp_list.append(s[line_len * i])
                else:
                    break
                for j in range(line_len):
                    if (line_len * i + j < len(s)):
                        tmp_list.append(s[line_len * i + j])
                if(len(tmp_list)>numRows):
                    tmp_list_full=tmp_list[:numRows]
                    sq_list.append(tmp_list_full)
                    for k in range(len(tmp_list)-numRows):
                        col_list_tmp=col_list[:]
                        col_list_tmp[numRows-1-k]=tmp_list[numRows+k]
                        sq_list.append(col_list_tmp)
                else:
                    tmp_list_full=tmp_list[:]
                    sq_list.append(tmp_list_full)
            res_s = ''
            for i in range(numRows):
                for j in range(len(sq_list)):
                    tmp_s = sq_list[j][i]
                    res_s += tmp_s

            res_s = res_s.replace(' ', '')
            return res_s


if __name__=='__main__':
    s='ABCD'
    so=Solution()
    res_s=so.convert(s,2)
    print(res_s)
