import math
def CreateCylinder(Segments,radius,height):
    
    #Fail cases
    if Segments <= 2: #Must have atleast 3 segments
        return False   
    
    Vertexes = [
        "v " + str(0) + " " + str(height / 2) + " " + str(0), #Top center vertex premade
    ]
    Faces = []
    
    AnglePerSeg = (math.pi * 2) / Segments
        
    #Vertex of circle
    for i in range(Segments):
        Vertexes.append("v " + str(math.sin(i * AnglePerSeg) * radius) + " " + str(-height / 2) + " " + str(math.cos(i * AnglePerSeg) * radius))
    
    Vertexes.append("v " + str(0) + " " + str(-height / 2) + " " + str(0))
    
    #Faces of circle
    for i in range(0,Segments):
        #Connection to top
        Faces.append("f " + str(1) + " " + str(i + 2) + " " + str((i + 1) % (Segments) + 2))
        #Connection to bottom
        Faces.append("f " + str(Segments + 1) + " " + str((i + 1) % (Segments) + 2) + " " + str(i + 2))

    print("Vertexes (" + str(len(Vertexes)) + "):")
    for i in Vertexes:
        print(i)
    print("Faces (" + str(len(Faces)) + "):")
    for i in Faces:
        print(i)
    
    f = open("Cone.obj", "w")
    for i in Vertexes:
        f.write(i + "\n")
    for k in Faces:
        f.write(k + "\n")
    
    f.close()

if __name__ == "__main__":
    CreateCylinder(16,2,4)