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
    
    #Top of the cylinder.
    
    #Vertex top circle
    for i in range(Segments):
        Vertexes.append("v " + str(math.sin(i * AnglePerSeg) * radius) + " " + str(height / 2) + " " + str(math.cos(i * AnglePerSeg) * radius))
    
    #Faces top circle
    for i in range(0,Segments):
        Faces.append("f " + str(1) + " " + str(i + 2) + " " + str((i + 1) % (Segments) + 2))
    
    #Top done!
    
    #Adds bottom center vertex.
    Vertexes.append("v 0 " + str(-height / 2) + " 0") 
    
    #Vertex bottom circle
    for i in range(Segments):
        Vertexes.append("v " + str(math.sin(i * AnglePerSeg) * radius) + " " + str(-height / 2) + " " + str(math.cos(i * AnglePerSeg) * radius))
    
    #Facec bottom circle
    for i in range(0,Segments):
        Faces.append("f " + str(Segments + 2) + " "  + str((i + 1) % (Segments) + 2 + Segments + 1) + " " + str(i + 2 + Segments + 1))
    
    #Bottom done!
    
    #Faces of the sides.
    for i in range(0,Segments):
        Faces.append("f " + str(i + 2) + " "  + str(i + Segments + 1 + 2) + " " + str((i + 1) % Segments + Segments + 3))
    for i in range(0,Segments):
        Faces.append("f " + str(i + 2) + " " + str((i + 1) % Segments + Segments + 3) + " "  + str((i + 1) % Segments + 2))
         
    
    print("Vertexes (" + str(len(Vertexes)) + "):")
    for i in Vertexes:
        print(i)
    print("Faces (" + str(len(Faces)) + "):")
    for i in Faces:
        print(i)
    
    
    f = open("Cylinder.obj", "w")
    for i in Vertexes:
        f.write(i + "\n")
    for k in Faces:
        f.write(k + "\n")
    
    f.close()

if __name__ == "__main__":
    CreateCylinder(6,3,3)