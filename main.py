# -*- coding: utf-8 -*-
from PIL import Image
# 调用removebg模块
from removebg import RemoveBg

rmbg = RemoveBg('SZiFJVwE4Q9xzRH39hn8obzS', 'error.log')
BACKGROUND_COLOR = {
    'RED': (255, 0, 0, 255),
    'BLUE': (67, 142, 219, 255),
    'WHITE': (255, 255, 255, 255)}

old_img = './JobPic.jpg'
new_img = './JobPic-new.png'
img = Image.open(old_img)
# 读取照片尺寸
(x, y) = img.size
# 重新设置照片尺寸
x_s = 295  # 宽
y_s = 413  # 高
out = img.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
out.save(new_img)

print('原始照片尺寸(宽x高): ', x, "x", y)
print('调整后照片尺寸:(宽x高) ', x_s, "x", y_s)


# 生成红色背景证件照
# 老照片路径、新照片路径、无背景照片路径、颜色
def get_img_bg(old_img_path, color):
    # 去掉背景图,提取照片
    rmbg.remove_background_from_img_file(old_img_path)  # 新生成一张追加尾缀_no_bg.png的pic
    foreground = Image.open("{}{}".format(old_img_path, "_no_bg.png"))
    background = Image.new('RGBA', foreground.size, BACKGROUND_COLOR[color])
    background.paste(foreground, mask=foreground)
    # background.show()
    background.save("{}{}".format(old_img_path[0:-4], "_{}.png".format(color)))

get_img_bg(old_img, 'RED')
get_img_bg(old_img, 'BLUE')
