from PIL import Image

def enc():

    img = Image.open("/tmp/temple.jpg")
    print(img.getpixel((0,0)))
    #img1 = img.copy()
    img.putpixel((0,0),(10,10,10))
    print(img.getpixel((0,0)))
    img.save("/tmp/abc.png", quality='keep')

def dec():
    img = Image.open("/tmp/abc.png")
    print(img.getpixel((0,0)))

dec()