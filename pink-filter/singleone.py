from PIL import Image
import os

directory = '.'
count = 1

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(filename)
        img = Image.open(f"{directory}/{filename}").convert('RGB')
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                # Apply multipliers to get a pink shade
                r = int(r * 1.8)  # Increase red intensity
                g = int(g * 0.7)  # Decrease green intensity
                b = int(b * 0.7)  # Decrease blue intensity
                img.putpixel((x, y), (r, g, b))

        img.save(f"{directory}{'/'}{'pink'}{filename}")
        count = count + 1

