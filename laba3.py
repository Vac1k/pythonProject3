import math
from PIL import Image, ImageDraw

picture = Image.new('RGB', (960, 960), (255,255,255))
paint = ImageDraw.Draw(picture)
angle = math.radians(20) #angel = 10*(1+1)

with open(r"C:\Users\vacik\Downloads\DS1.txt","r") as file:
    for line in file:
        y_x = line.split()
        Yj = int(y_x[0]) - 480
        Xi = int(y_x[1]) - 480
        x = Xi * math.cos(angle) - Yj * math.sin(angle)
        y = Xi * math.sin(angle) + Yj * math.cos(angle)
        paint.point((x + 480, y + 480, x + 481, y + 481), fill=(0, 0, 255))

picture.show()
picture.save("finalpicture.png")