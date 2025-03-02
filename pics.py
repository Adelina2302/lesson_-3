from PIL import Image


image = Image.open("monro.jpg")
red, green, blue = image.split()


red_cropped1 = red.crop((50, 0, red.width, red.height))
red_cropped2 = red.crop((25, 0, red.width - 25, red.height))
image1 = Image.blend(red_cropped1, red_cropped2, 0.6)

blue_cropped1 = blue.crop((0, 0, blue.width - 50, blue.height))
blue_cropped2 = blue.crop((25, 0, blue.width - 25, blue.height))
image2 = Image.blend(blue_cropped1, blue_cropped2, 0.6)

image3 = green.crop((25, 0, green.width - 25, green.height))


monro_3colors = Image.merge("RGB", (image1, image2, image3))
monro_3colors.save("monro_3colors.jpg")


monro_3colors.thumbnail((80, 80))
monro_3colors.save("final_monro.jpg")