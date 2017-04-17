from PIL import Image,ImageDraw,ImageFont
img=Image.open("F:\Python练习\表情包制作\di.jpg")
jgz=Image.open("F:\Python练习\表情包制作\shang.jpg")
img.paste(jgz,(73,42))
##img.show()

draw=ImageDraw.Draw(img)
ttfront=ImageFont.truetype('simhei.ttf',24)
draw.text((32,190)," 内心毫无波澜\n  甚至还想笑",fill=(0,0,0),font=ttfront)
img.show()
img.save("F:\Python练习\表情包制作\生成的表情包.jpg")