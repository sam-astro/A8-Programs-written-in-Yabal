import sys

vertexes = []
faces = []



def rescale(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))

file = open(sys.argv[1], "r")
file2 = open(sys.argv[1], "r")

# find range of vertex coordinates for use with scaling
vMin = 100
vMax = 0
for line in file:
    parts = line.strip().split(' ')

    if parts[0] == 'v':
        x = float(parts[1])
        y = float(parts[2])
        z = float(parts[3])
        if x > vMax:
            vMax = x
        if y > vMax:
            vMax = y
        if z > vMax:
            vMax = z
        if x < vMin:
            vMin = x
        if y < vMin:
            vMin = y
        if z < vMin:
            vMin = z

v = 0
f = 0
fwr = open(sys.argv[1] + ".a3d", "w")
ybl = open(sys.argv[1] + ".yabal", "w")
for line in file2:
    parts = line.strip().split(' ')

    if parts[0] == 'v':
        x = int(rescale(float(parts[1]), vMin, vMax, 20, 93))
        y = int(rescale(float(parts[2]), vMin, vMax, 20, 93))
        z = int(rescale(float(parts[3]), vMin, vMax, 20, 93))

        print("v " + str(x) + " " + str(y) + " " + str(z))
        fwr.write("v " + str(x) + " " + str(y) + " " + str(z) + "\n")
        ybl.write("pointsXY[" + str(v) + "] = {x : " + str(x) + ", y : " + str(y) + "};\n")
        ybl.write("pointsZ[" + str(v) + "] = " + str(z) + ";\n")
        v += 1

    if parts[0] == 'f':
        f1 = int(parts[1].split('/')[0])
        f2 = int(parts[2].split('/')[0])
        f3 = int(parts[3].split('/')[0])

        print("f " + str(f1-1) + " " + str(f2-1) + " " + str(f3-1))
        fwr.write("f " + str(f1-1) + " " + str(f2-1) + " " + str(f3-1) + "\n")
        ybl.write("facesX[" + str(f) + "] = " + str(f1-1) + ";\n")
        ybl.write("facesY[" + str(f) + "] = " + str(f2-1) + ";\n")
        ybl.write("facesZ[" + str(f) + "] = " + str(f3-1) + ";\n")
        f += 1

ybl.write("numberOfPoints = " + str(v) + ";\n")
ybl.write("numberOfFaces = " + str(f) + ";\n")

fwr.close()
ybl.close()