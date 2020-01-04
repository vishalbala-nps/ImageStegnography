import sys
from PIL import Image
#Functions Here
def printusage():
    print("USAGE:")
    print("stegnographer.py -e|-d [IMAGE FILE NAME]")
    exit(1)

def changepix(imgdata, x=0, y=0, val=0):
    print("Changepix:")
    r,g,b = getpix(imgdata, x, y)
    r = val
    colors = (r,g,b)
    imgdata.putpixel((x,y),colors)
    print(imgdata.getpixel((x,y)))

def getpix(imgdata, x=0, y=0):
    print("getpix:")
    r,g,b = imgdata.getpixel((x,y))
    colors = (r,g,b)
    print(colors)
    return colors

def encryptimg(fname):
    print("Encrypt")
    try:
        img = Image.open(fname)
        print(img.mode)
        img_copy = img.copy()
    except:
        print("Unable to open the image! Please check the filename and the permisions and try again")
        exit(1)

    msg = input("Enter a message (max 255 chars):")
    changepix(img_copy, val=100)
    img_copy.save(fname, 'PNG')
    

def decryptimg(fname):
    print("Decrypt")
    try:
        img = Image.open(fname)
    except Exception as e:
        print(e)
        print("Unable to open the image! Please check the filename and the permisions and try again")
        exit(1)
    getpix(img)

#Main Program Starts Here
if len(sys.argv) != 3:
    print("Invalid number of arguments!")
    printusage()

option = sys.argv[1]
fname = sys.argv[2]

if option == "-e":
    encryptimg(fname)
elif option == "-d":
    decryptimg(fname)
else:
    print("Invalid Arguments!")
    printusage()
