from PIL import Image, ImageDraw
import numpy as num

#loading the image
path_of_image = 'Genos.jpg'

# Converting to grayscale
image = Image.open(path_of_image).convert('L')

# Convert image --> numpy array
image_array = num.array(image)

# Creating white background
dot_image = Image.new('RGB', image.size, 'white')
draw = ImageDraw.Draw(dot_image)
dot_size = 2

# Draw dots in specific positions
for x in range(image_array.shape[1]):
    for y in range(image_array.shape[0]):
        brightness = image_array[y,x]
        if brightness < 120:
            draw.ellipse((x-dot_size//2, y-dot_size//2, x+dot_size//2, y+dot_size//2), fill='black')
dot_image.show()
