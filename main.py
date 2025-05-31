from PIL import Image

monro = Image.open('monro.jpg')

blend_max = 0.3

red, green, blue = monro.split()

red_crop = red.crop((100,0,red.width, red.height))
red_crop_2 = red.crop((50,0,red.width-50, red.height))
new_red = Image.blend(red_crop, red_crop_2, blend_max)


blue_crop = blue.crop((0,0,blue.width-100, blue.height))
blue_crop_2 = blue.crop((50,0,blue.width-50, blue.height))
new_blue = Image.blend(blue_crop, blue_crop_2, blend_max)

green_crop = green.crop((50,0,green.width-50, green.height))

monro_blend = Image.merge ("RGB", (new_red, green_crop, new_blue))
monro_blend.save('monro_blend.jpg')

monro_blend.thumbnail((80, 80))
monro_blend.save('monro_blend_resize.jpg')

