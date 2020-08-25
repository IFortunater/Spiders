from PIL import Image
import requests

img_url = "https://so.gushiwen.cn//RandCode.ashx"
img_content = requests.get(img_url).content
with open("验证码.jpg", 'wb') as f:
    f.write(img_content)
    f.close()
img = Image.open("验证码.jpg")
print(img.show())