import pytesseract
from PIL import Image

pytesseract.tesseract_cmd = r'C:\Users\CRI\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
img = Image.open("C:\\Users\\CRI\\Downloads\\1.jpg")

output = pytesseract.image_to_data(img)


print(output)