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

def writemsglen(imgdata, length, dimensions):
    x = int(dimensions[0])-1
    y = int(dimensions[1])-1
    changepix(imgdata, x=x, y=y, val=length)

def getmsglen(imgdata, dimensions):
    x = int(dimensions[0])-1
    y = int(dimensions[1])-1
    colors = getpix(imgdata, x=x, y=y)
    return int(colors[0]) 


def encryptimg(fname):
    print("Encrypt")
    try:
        img = Image.open(fname)
        if img.mode != "RGB":
            img = img.convert('RGB')
            print(img.mode)

    except:
        print("Unable to open the image! Please check the filename and the permisions and try again")
        exit(1)

    msg = input("Enter a message (max 255 chars):")
    msglen = len(msg)
    if msglen > 255:
        print("Message is greater than 255 charecters!")
        exit(1)
    else:
        writemsglen(img, msglen, img.size)
        img.save(fname, 'PNG')
    

def decryptimg(fname):
    print("Decrypt")
    try:
        img = Image.open(fname)
    except Exception as e:
        print(e)
        print("Unable to open the image! Please check the filename and the permisions and try again")
        exit(1)
    print("Message is of length:"+str(getmsglen(img, img.size)))

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
