## -------------------- Ball Generator ------------------------- ##
#Written By: Aarni Junkkala
import math

def CreateBall(Segments = 16,Rings = 16,Radius = 1, PosX = 0, PosY = 0, PosZ = 0):
    #Rings are created with idea that single top vertex is considered to be a one ring,
    #and bottom single vertex isn't
    if Segments <= 2 or Rings <= 2:
        return False
    
    #Rotation to radians
    RotX = RotX * math.pi / 180
    RotY = RotY * math.pi / 180
    RotZ = RotZ * math.pi / 180
    
    print(RotX,RotY,RotZ)
    
    
    Vertexes = [
        "v " + str(PosX) + " " + str(Radius + PosY) + " " + str(PosZ)
    ]

    #Distances between segments.
    AnglePerSeg = (math.pi * 2) / Segments

    #Vertexes for sides.
    for i in range(1,Rings):
        for k in range(Segments):
            CenterDist = math.cos(math.asin(math.cos((i/Rings)* math.pi))) * Radius
            Vertexes.append("v " + str(math.sin(AnglePerSeg * k) * CenterDist + PosX) + " " + str(math.cos((i/Rings)* math.pi) * Radius + PosY) + " " + str(math.cos(AnglePerSeg * k) * CenterDist + PosZ))
    
    #Bottom Vertex
    Vertexes.append("v " + str(PosX) + " " + str(-Radius + PosY) + " " + str(PosZ))

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

    #Writes to file
    f = open("Ball.obj", "w")
    for i in Vertexes:
        f.write(i + "\n")
    for k in Faces:
        f.write(k + "\n")
    
    f.close()
    print("Ball created succesfully!")
    
if __name__ == "__main__":
    CreateBall(16,16,2)