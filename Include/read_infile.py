import pandas as pd
import os


def read_infile(pathin):
    # 读取待录入文件的文件名
    filelist = os.listdir(pathin)
    print('待录入的文件:')
    print(filelist)
    # 拼接待录入文件的路径
    path = pathin + "/" + filelist[0]
    print(path)
    # 表格起始时间
    sheet = pd.read_excel(path, sheet_name=0)
    # begintime = sheet['时间'][1]
    return sheet
