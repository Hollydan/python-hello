
#check robot
import pytesseract as pt
from PIL import Image

image = Image.open('1.png')

text = pt.image_to_string(image)

print(text)
