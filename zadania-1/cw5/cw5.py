import random

set1 = set()
set2 = set()

for i in range(20):
    set1.add(i)
    set2.add(random.randint(0,30))

print("Sekwencja pierwsza: ", set1)
print("Sekwencja druga: ", set2, end="\n\n")

print("Elementy będące w obu sekwencjach na raz: ", set1.intersection(set2))
print("Złączone sekwencje bez powtórzeń: ", set1.union(set2))