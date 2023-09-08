import urllib

import discord
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from urllib import request


class CreateProfileImage:
    def __init__(self):
        self.pathToImages = "./Images/"

    def getImage(self, user, background):
        background = background
        image = Image.open(self.pathToImages + background + ".png")

        image = self.__roundRectangle(image)

        image.paste(self.__getProfilePicture(user), (120, 120))
        image_with_text = self.__addValues(image)

        with BytesIO() as image_binary:
            image_with_text.save(image_binary, 'PNG')
            image_binary.seek(0)
            image_file = discord.File(fp=image_binary, filename="profile.png")
            return image_file

    def __getProfilePicture(self, user):
        pfp_url = user.display_avatar.url
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent}
        requestPfp = urllib.request.Request(pfp_url, None, headers)
        pfp = Image.open(urllib.request.urlopen(requestPfp))
        pfp = pfp.resize(size=(512, 512))
        return pfp

    def __addValues(self, image):
        d1 = ImageDraw.Draw(image)
        font_size = 256  # Erhöhte Schriftgröße
        font = ImageFont.truetype("arial.ttf", font_size)  # Schriftart auswählen
        d1.text((800, 120 + (512/2) - (font_size/2)), "Test", fill=(0, 0, 0), font=font, stroke_width=1, spacing=100)
        return image

    def __roundRectangle(self, im):

        rad = 120

        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        alpha = Image.new('L', im.size, "white")
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im
