grid ='+'
width = int(input("Podaj szerokość: "))
height = int(input("Podaj wysokość: "))

for i in range(width):
    grid += '---+'

for j in range(height):
    grid += '\n|'

    for i in range(width):
        grid += '   |'

    grid += '\n+'

    for i in range(width):
        grid += '---+'

print(grid,end='\n')