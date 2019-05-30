from PIL import ImageEnhance
from PIL import Image

image = Image.open('.png') # Specifiy the image which is needed to be open  .

sharper = ImageEnhance.Color(image) # This fuction is used to change the color
image = sharper.enhance(0) #An enhancement factor of 0.0 gives a black and white image andfactor of 1.0 gives the original image.

sharper = ImageEnhance.Brightness(image) # This function is used for the increasing th bightness of the image . 
image = sharper.enhance(5) # An Enhancement factor of 0.0 gives a black image and factor of 1.0 gives the original image.

sharper = ImageEnhance.Contrast(image) # This function helps to increase the contrast of the give image .
image = sharper.enhance(3) # An Enhancement factor of 0.0 gives a solid grey image and factor of 1.0 gives the original image.

image.save('test.png') # At the output this will save the image with a name (any name as per the user ) which will be stored in the current folder only .

