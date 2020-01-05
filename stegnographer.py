import sys
from PIL import Image
#Functions Here
def printusage():
    print("USAGE:")
    print("stegnographer.py -e|-d [IMAGE FILE NAME]")
    exit(1)

def changepix(imgdata, x=0, y=0, val=0):
    r,g,b = getpix(imgdata, x, y)
    r = val
    colors = (r,g,b)
    imgdata.putpixel((x,y),colors)

def getpix(imgdata, x=0, y=0):
    r,g,b = imgdata.getpixel((x,y))
    colors = (r,g,b)
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

def getco(size, counter):
    x = int(counter/size[1])
    y = int(counter%size[1])
    return (x,y)

def encryptimg(fname):
    try:
        img = Image.open(fname)
        if img.mode != "RGB":
            img = img.convert('RGB')

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
        counter = 0
        for i in msg:
            xval, yval = getco(img.size, counter)
            changepix(img, x=xval, y=yval, val=ord(i))
            counter = counter + 1
        img.save(fname, 'PNG')
    

def decryptimg(fname):
    try:
        img = Image.open(fname)
    except Exception as e:
        print(e)
        print("Unable to open the image! Please check the filename and the permisions and try again")
        exit(1)
    msglen = getmsglen(img, img.size)
    print("Message is of length:"+str(msglen))
    counter = 0
    msglist = []
    while counter < msglen:
        xval, yval = getco(img.size, counter)
        msglist.append(chr(getpix(img, x=xval ,y=yval)[0]))
        counter = counter + 1
    smsg = "" 
    print(smsg.join(msglist))

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
