from PIL import Image, ImageChops

# Load the images
im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")

# XOR using ImageChops
# im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
# https://stackoverflow.com/questions/19341500/importing-python-modules-imagechops
im3 = ImageChops.difference(im1, im2)

# save
im3.save("./flag-decode.png")