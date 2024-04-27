from PIL import Image
import sys

im = Image.open(sys.argv[2])
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

fileLines = []

codeOut = False

if sys.argv[3] == "code":
    codeOut = True
    fileLines.append("asm{\n")

if sys.argv[1] == "height":
    for y in range(0,im.size[1]):
        pxCount = 0
        for x in range(0,im.size[0]):
            bwv = int(pix[x,y][0]/8)&0b11111

            #print("hex out " + hex((redv << 5) | (greenv << 2) | bluev).lstrip("0x"))
            hexStr = hex(bwv).lstrip("0x")
            while len(hexStr) < 2:
                hexStr = "0" + hexStr
            if codeOut == False:
                fileLines.append(hexStr)
            else:
                #fileLines.append("heightmapBuffer[" + str(x+y*108) + "] = " + str(bwv) + ";\n")
                fileLines.append("set " + str(x+y*108+21000) + " " + str(bwv) + "\n")

elif sys.argv[1] == "color":
    for y in range(0,im.size[1]):
        pxCount = 0
        for x in range(0,im.size[0]):
            print("r: " + str(pix[x,y][0]) + "  g: " + str(pix[x,y][1]) + " b: " + str(pix[x,y][2]), end=", ")
            redv = 0b111&int(pix[x,y][0]/255.0*7.0)+1
            greenv = 0b111&int(pix[x,y][1]/255.0*7.0)+1
            bluev = 0b11&int(pix[x,y][2]/255.0*3.0)+1

            print("rv: " + str(redv) + "  gv: " + str(greenv) + " bv: " + str(bluev), end=", ")


            #print("hex out " + hex((redv << 5) | (greenv << 2) | bluev).lstrip("0x"))
            hexStr = hex((redv << 5) | (greenv << 2) | bluev).lstrip("0x")
            while len(hexStr) < 2:
                hexStr = "0" + hexStr
            if codeOut == False:
                fileLines.append(hexStr)
            else:
                #fileLines.append("colormapBuffer[" + str(x+y*108) + "] = " + str((redv << 5) | (greenv << 2) | bluev) + ";\n")
                fileLines.append("set " + str(x+y*108+32664) + " " + str((redv << 5) | (greenv << 2) | bluev) + "\n")

            print("hex: " + hexStr)

if codeOut:
    fileLines.append("};")
    with open(sys.argv[1] + ".yabal", 'w') as f:
        for line in fileLines:
            f.write(line)
else:
    with open(sys.argv[1] + ".lst", 'w') as f:
        for line in fileLines:
            f.write(line)