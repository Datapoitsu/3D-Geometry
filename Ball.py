## -------------------- Ball Generator ------------------------- ##
#Written By: Aarni Junkkala

import math

def CreateBall(Segments,Rings,Radius):
    #Rings are created with idea that single top vertex is considered to be a one ring,
    #and bottom single vertex isn't
    if Segments <= 2 or Rings <= 2:
        return False
    
    Vertexes = [
        "v 0 " + str(Radius) + " 0"
    ]

    #Distances between rings and segments.
    RingDistance = Radius * 2 / Rings
    AnglePerSeg = (math.pi * 2) / Segments

    #Vertexes for sides.
    for i in range(1,Rings):
        for k in range(Segments):
            CenterDist = math.cos(math.asin(Radius - (i * RingDistance)))
            Vertexes.append("v " + str(math.sin(AnglePerSeg * k) * CenterDist) + " " + str(Radius - i * RingDistance) + " " + str(math.cos(AnglePerSeg * k) * CenterDist))
    
    Vertexes.append("v 0 " + str(-Radius) + " 0")

    #Faces
    Faces = []

    #Faces on top
    for i in range(Segments):
        Faces.append("f 1 " + str(i + 2) + " " + str((i + 1) % Segments + 2))

    #Faces on sides
    for i in range(Rings - 2):
        for k in range(0,Segments):
            Faces.append("f " + str(i * Segments + 2 + k) + " " + str(2 + k + (i + 1) * Segments) + " " + str(2 + (k + 1) % Segments + (i + 1) * Segments))
            Faces.append("f " + str(i * Segments + 2 + k) + " " + str(i * Segments + 2 + (k + 1) % Segments + Segments) + " " + str(i * Segments + 2 + (k + 1) % Segments))

    #Faces on bottom
    for i in range(Segments):
        Faces.append("f " + str(len(Vertexes)) + " " + str(len(Vertexes) - 1 - i) + " " + str(len(Vertexes) + (-i - 2) % Segments - Segments))
        print(Faces[-1])

    #Writes to file
    f = open("Ball.obj", "w")
    for i in Vertexes:
        f.write(i + "\n")
    for k in Faces:
        f.write(k + "\n")
    
    f.close()

if __name__ == "__main__":
    CreateBall(64,64,1)