import requests, base64, re , qrcode, io
from PIL import Image, ImageDraw, ImageFont

""" # 图片转RGB  # 创建一个可以在给定图像上绘图的对象
    # 字体的格式，中文要中文字体       # 绘制文本 """
def image_add_text(img, text, left, top, text_color=(255, 0, 0), text_size=13):
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)
    fontStyle = ImageFont.truetype("FreeMono.ttf", text_size, encoding="utf-8")
    draw.text((left, top), text, text_color, font=fontStyle)
    return img

def print_md(text, file):
    print("![%s](./png/%s)\n" % (text , file))

url = 'https://m.262235.xyz/USA'
r = requests.get(url)
s = base64.b64decode(r.text).decode('ascii')
vms = s.split('\n')

for i in range(len(vms)-1):
    img = qrcode.make(vms[i])
    text = vms[i][:32]
    img = image_add_text(img, text , 50, 2 , text_color=(50,50,50), text_size=24)
    text = text[:10].replace("://", "_")
    file = str(i) + '_'+ text  +'.png'
    img.save('./png/' + file)
    print_md(vms[i][:32] , file)