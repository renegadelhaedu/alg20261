#instalar pacotes
#pip install nome_pacote
from PIL import Image, ImageFilter

with Image.open("prof.jpg") as im:
    im = im.convert("L")


out = im.filter(ImageFilter.DETAIL)
out.show()