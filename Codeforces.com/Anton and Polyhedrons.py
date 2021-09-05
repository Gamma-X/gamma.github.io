face=0
for i in range(int(input())):
    polyh=input()
    if polyh=="Tetrahedron":
        face=face+4
    if polyh=="Cube":  
        face=face+6
    if polyh=="Octahedron":
        face=face+8
    if polyh=="Dodecahedron":
        face=face+12
    if polyh=="Icosahedron":
        face=face+20
print(face)
