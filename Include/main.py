import pandas as pd
import os

def updaterow(row,numofcol):
    i=1
    print('-----------------------------------------------------------------')
    # print(type(row))
    while i<numofcol:
        # print(row[1][i])
        if row[1][i] =='-':
            # print('-')
            row[1][i]=0
        i=i+1
    return row




# 填充空的数
def updatedata(path):
    df = pd.read_excel(path, sheet_name=0)
    numofcol,numofrow=df.shape
    result=()
    for row in df.iteritems():
         newrow = updaterow(row,numofcol)  # 每一列填充空位
         result =result+newrow
    print(result)
    df_result = pd.DataFrame(result)
    df_result.to_excel("D:/test.xls",index=False)




if __name__ == '__main__':
    path = "D:/CXCDATA/yibanyuanchuanbiaover0.xls"#待录入文件的路径
    updatedata(path)
