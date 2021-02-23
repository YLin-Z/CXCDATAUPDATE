import pandas as pd
import os

def updaterow(row,numofcol):
    i=0
    while i<=numofcol:
        print(i)
        print(row[i])
        i=i+1





# 填充空的数
def updatedata(path):
    df = pd.read_excel(path, sheet_name=0)
    numofcol,numofrow=df.shape
    for row in df.iteritems():
        # print('正在处理:')
        # print(row[0])
        updaterow(row,numofcol)  # 每一列填充空位



if __name__ == '__main__':
    path = "D:/CXCDATA/yibanyuanchuanbiao.xls"#待录入文件的路径
    updatedata(path)
