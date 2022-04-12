# petit code qui génère des barres parallèles
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint
nb_img = 30


for i in range(nb_img):
    epsilon = randint(3, 5)
    for j in range(5):
        img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
        if j == 4:
            angle = randint(0, 180)
            foreground = Image.open("barre.png").rotate(angle, resample=3, expand=True)
            x = randint(0, get_monitors()[0].width - 700)
            y = randint(0, get_monitors()[0].height - 700)
            img.paste(foreground, (x, y),
                      foreground)
            foreground = Image.open("barre.png").rotate(angle+epsilon, expand=True)
            img.paste(foreground, (x + randint(150, 400), y + randint(150, 400)),
                      foreground)
        else:
            foreground = Image.open("barre.png").rotate(45, expand=True)
            x = randint(0, get_monitors()[0].width - 700)
            y = randint(0, get_monitors()[0].height - 700)
            img.paste(foreground, (x, y), foreground)
            img.paste(foreground, (x + randint(150, 400), y + randint(150, 400)), foreground)
        img.save(f"img/img_{i}_{j}.png")
