# x = 22
# print("\nOriginal Number: ", x)
# print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
# print("Right aligned (width 10)  :"+"{:10d}".format(x));
# print("Center aligned (width 10) :"+"{:^10d}".format(x));

x = int(input("Podaj długość miarki: "))

measure = '|'

for j in range(x):
    measure +=" . . . . |"

measure +="\n0"

for i in range(x):
    measure += "{:10d}".format(i+1)

print(measure)
