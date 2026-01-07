# ASCII Art Project - Image to ASCII Conversion
# Uses loops, conditions and logical thinking

from PIL import Image

# characters arranged from dark to light
symbols = "@#%*+=-:. "

# canvas size (length of output)
output_width = 90        # number of columns (length of each row)
output_height = 0        # this will be updated after resizing

# resize image using proportional scaling
def resize_image(img, new_width):
    global output_height
    w, h = img.size
    ratio = h / w
    output_height = int(new_width * ratio * 0.60)   # number of rows
    return img.resize((new_width, output_height))

# convert pixel value (0–255) into a symbol
def map_pixel_to_char(pixel):
    step = 256 // len(symbols)
    index = pixel // step
    if index >= len(symbols):
        index = len(symbols) - 1
    return symbols[index]

# main function
def generate_ascii(path):
    img = Image.open(path)

    # resizing and grayscale conversion
    img = resize_image(img, output_width)
    img = img.convert("L")

    pixels = img.getdata()
    width, height = img.size
    k = 0

    print("ASCII Image Size:")
    print("Rows (Height)  =", height)
    print("Columns (Width) =", width)
    print("---------------------------------\n")

    # print ASCII art using nested loops
    for r in range(height):
        row_chars = ""
        for c in range(width):
            pixel = pixels[k]
            row_chars += map_pixel_to_char(pixel)
            k += 1
        print(row_chars)

# program execution
generate_ascii("anushka.jpg")
