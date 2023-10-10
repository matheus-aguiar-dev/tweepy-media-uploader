from PIL import Image, ImageEnhance
import os

directory = 'edited'
dirImage = 'manga'
count = 1

for filename in os.listdir(dirImage):
    if filename.endswith(".jpg"):
        print(filename)
        img = Image.open(f"{dirImage}/{filename}").convert('RGB')
        width, height = img.size

        # Increase brightness

        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))

                # Apply multipliers to get a pink shade with preserved lightness
                r = int(r * 1.8)  # Increase red intensity
                g = int(g * 0.6)  # Decrease green intensity (preserving some lightness)
                b = int(b * 0.75)  # Decrease blue intensity (preserving some lightness)
                img.putpixel((x, y), (r, g, b))


        enhancer_brightness = ImageEnhance.Brightness(img)
        img = enhancer_brightness.enhance(1.45)  # Increase brightness (adjust the factor as needed)

        # Increase vibrance
        enhancer_vibrance = ImageEnhance.Color(img)
        img = enhancer_vibrance.enhance(1.8)  # Increase vibrance (adjust the factor as needed)
        img.save(f"{directory}/{count}.jpg")
        count = count + 1

