from PIL import Image
import os

directory = 'edited'
dirImage = 'manga'
count = 1

for filename in os.listdir(dirImage):
    if filename.endswith(".jpg"):
        print(filename)
        img = Image.open(f"{dirImage}/{filename}").convert('RGB')
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                # Apply multipliers to get a pink shade with preserved lightness
                r = int(r * 1.8)  # Increase red intensity
                g = int(g * 0.9)  # Decrease green intensity (preserving some lightness)
                b = int(b * 0.9)  # Decrease blue intensity (preserving some lightness)
                img.putpixel((x, y), (r, g, b))

        img.save(f"{directory}{'/'}{count}{'.jpg'}")
        count = count+1
# img.save(f"{directory}\{'1.jpg'}")
