import pytesseract
from PIL import Image
img = Image.open("pics/b5A7j.png")
print(pytesseract.image_to_string(img))
