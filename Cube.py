def CreateCube(xMult,yMult,zMult):
    Vertexes = [
        "v " + str(xMult) + " " + str(yMult) + " " + str(zMult),
        "v " + str(xMult) + " " + str(yMult) + " " + str(-zMult),
        "v " + str(-xMult) + " " + str(yMult) + " " + str(-zMult),
        "v " + str(-xMult) + " " + str(yMult) + " " + str(zMult),
        
        "v " + str(xMult) + " " + str(-yMult) + " " + str(zMult),
        "v " + str(xMult) + " " + str(-yMult) + " " + str(-zMult),
        "v " + str(-xMult) + " " + str(-yMult) + " " + str(-zMult),
        "v " + str(-xMult) + " " + str(-yMult) + " " + str(zMult),
    ]
    
    Faces = [
        "f 1 5 2",
        "f 2 6 3",
        "f 3 7 4",
        "f 4 8 1",
        
        "f 5 6 2",
        "f 6 7 3",
        "f 7 8 4",
        "f 8 5 1",
        
        "f 1 2 3",
        "f 3 4 1",
        "f 5 7 6",
        "f 7 5 8",       
    ]
    
    f = open("Cube.obj", "w")
    for i in Vertexes:
        f.write(i + "\n")
    for k in Faces:
        f.write(k + "\n")
    
    f.close()

if __name__ == "__main__":
    CreateCube(1,1,1)