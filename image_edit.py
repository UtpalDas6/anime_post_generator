from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random_quotes import get_random_quote
import random

def render_image():
    lis=list(range(1,15))
    ch=random.choice(lis)
    img = Image.open("bg"+str(ch)+".jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("C:\Windows\Fonts\ARLRDBD.TTF", 40)
    # draw.text((x, y),"Sample Text",(r,g,b))
    quote = get_random_quote()
    print(quote)
    quote=quote.split('\n')
    quote[0]=quote[0].replace(' ', '\n')
    quote[1]=quote[1].replace('[','\n[')
    quote=quote[0]+'\n'+quote[1]
    print(quote)
    draw.text((10, 10),quote,(255,255,255),font=font)
    img.save('sample-out.jpg')