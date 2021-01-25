import pandas as pd
import os
from read_infile import read_infile
from write_outfile import write_outfile


def upmissvalue(pathout):
    pass

def dropdown(pathout):
    pass


if __name__ == '__main__':
    pathin = "d:/IN_cxcdata"#待录入文件的路径
    pathout = {'dongsha':"d:/OUT_cxcdata/dongsha.xls",
               'nanjiaoshaluo':"d:/OUT_cxcdata/shaluo_nanjiao.xls"}  # 目标文件的路径
    #读取待录入的文件
    sheet = read_infile(pathin)
    # 将每一列写入对的位置
    write_outfile(sheet,pathout)
    #实现原下拉功能的计算时流量
    dropdown(pathout)
    #补全缺失数据
    upmissvalue(pathout)
    #判断有没有流量计改变流向