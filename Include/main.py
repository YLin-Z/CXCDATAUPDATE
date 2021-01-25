import pandas as pd
import os


def read_infile(pathin,pathout):
    filelist = os.listdir(pathin)
    print('待录入的文件:')
    print(filelist)
    print('待录入的文件数量:')
    print(len(filelist))
    path = pathin + "/" + filelist[0]
    print(path)
    # 写入目标文件
    write_outfile(path,pathout)


def write_outfile(path,pathout):
    sheet = pd.read_excel(path,sheet_name = 0)
    begintime = sheet['时间'][1]
    a = sheet[1:]
    print(a)
    print(begintime)



def dropdown(pathout):
    pass


def upmissvalue(pathout):
    pass


if __name__ == '__main__':
    pathin = "d:/IN_cxcdata"#待录入文件的路径
    pathout = "d:/OUT_cxcdata"  # 目标文件的路径
    #读取待录入的文件列表,并遍历写入
    infilelist = read_infile(pathin,pathout)
    #实现原下拉功能的计算时流量
    dropdown(pathout)
    #补全缺失数据
    upmissvalue(pathout)
    #判断有没有流量计改变流向