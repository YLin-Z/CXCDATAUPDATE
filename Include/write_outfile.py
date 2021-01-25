import pandas as pd
import os

def write_outfile(sheet,pathout):
    print(sheet.head(0))
    # 补全目标表格的时间列
    endtime = sheet.iloc[-1]['时间']#这是待录入数据的最后一个时间，也是最新的时间
    update_out_sheet_time(pathout['dongsha'],endtime)#更新东沙表格的时间列
    # write_one(3194,8,pathout+"/dongsha.xls",sheet)
    pass


#写入一个流量计
def write_one(in_name,out_name,pathout,sheet_in):
    begintime = sheet_in.iloc[1]['时间']
    sheet_out = pd.read_excel(pathout, sheet_name=1)
    i = 1
    while 1 == 1:
        try:
            print(sheet_in.iloc[i]['时间'])
            print(sheet_in.iloc[i][in_name])
            i = i + 1
        except IndexError:
            break
    del sheet_out
    del sheet_in

def update_out_sheet_time(path,endtime):
    sheet_out = pd.read_excel(path, sheet_name=1)
    if sheet_out.iloc[-1]['时间'] < endtime:
        print(sheet_out.iloc[-1]['时间'])
        df = pd.DataFrame({'时间':['2021-01-25 08:00:00','2021-01-25 09:00:00','2021-01-25 100:00:00']})
        sheet_out = pd.concat([sheet_out,df])
        sheet_out.to_excel('test.xls')
    else:
        print('不需要更新'+path+'时间')