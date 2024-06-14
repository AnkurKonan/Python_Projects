from PIL import Image

image_path = 'Ankur.jpeg'
image = Image.open(image_path)
width, height = image.size
grayscale_image = Image.new('L', (width, height))

for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_image.putpixel((x, y), gray)
grayscale_image.save('grayscale_image_manual.jpg')
grayscale_image.show()
