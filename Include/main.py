import pandas as pd
import os

def updaterow(row,numofcol):
    i=1
    print('-----------------------------------------------------------------')
    print(type(row))
    while i<numofcol-1:
        print(row[1][i])
        i=i+1




# 填充空的数
def updatedata(path):
    df = pd.read_excel(path, sheet_name=0)
    numofcol,numofrow=df.shape
    for row in df.iteritems():
         updaterow(row,numofcol)  # 每一列填充空位





if __name__ == '__main__':
    path = "D:/CXCDATA/yibanyuanchuanbiao.xls"#待录入文件的路径
    updatedata(path)
