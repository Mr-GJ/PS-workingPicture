# -*- coding: utf-8 -*-
# 所有的图片与PDF转换的操作都在这里进行定义

from multiprocessing import Pool
# 安装fitz需要安装PyMuPDF才能使用
import fitz
import os

# pdf路径
# tmp = r"D:\\Users\\Downloads\\"
tmp = r"."

export_file = r"./output"

save_path = r"./output"
os.makedirs(export_file, exist_ok=True)
pdf_dir = [i for i in os.listdir(tmp) if os.path.splitext(i)[-1] == ".pdf"]


def pdf_to_jpg(name):
    # lock.acquire()
    # 拼接pdf的文件路径
    pwd_name = os.path.join(tmp, name)
    with fitz.open(pwd_name) as doc:
        # 将文件名同我们的保存路径拼接起来（保存图片的文件夹）
        dir_name = os.path.splitext(name)[0]
        pdf_name = os.path.join(export_file, dir_name)
        # print(pdf_name)
        temp = 0
        # （保存图片的文件夹）不存咋则生成
        # exsitsdir.judge(pdf_name)
        os.makedirs(pdf_name, exist_ok=True)
        for pg in range(doc.page_count):
            page = doc[pg]
            temp += 1
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha=False)

            pic_name = '{}.jpg'.format(temp)
            # 拼接生成pdf的文件路径
            pic_pwd = os.path.join(pdf_name, pic_name)
            # print(pic_pwd)
            pm.save(pic_pwd)


def main():
    # pool = Pool(2)
    # for i in pdf_dir:
    #     res = pool.apply_async(pdf_to_jpg, (i,))
    # pool.close()
    # pool.join()
    for i in pdf_dir:
        pdf_to_jpg(i)

if __name__ == '__main__':
    main()  # 需要pdf切图就开启