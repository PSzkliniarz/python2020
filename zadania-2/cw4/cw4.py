def fun(x , y , z, n):
    # i <= x
    # j <= y
    # k <= z
    # i + j + k != n
    print("Wszystkie permutacje", [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) ])

    print("Nie sumujące się do ",n," ",
          [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

print("Wprowadź parametry:")
xx = int(input("X: "))
yy = int(input("Y: "))
zz = int(input("Z: "))
nn = int(input("N: "))
fun(xx,yy,zz,nn)