import time


class Bug:
    """A class that counts objects:"""
    counter = 0

    def __init__(self):
        self.__class__.counter += 1
        self.id = self.counter

    def __str__(self):
        return 'Counter: {self.counter}, id: {self.id}'.format(self=self)

    def __del__(self):
        self.__class__.counter -= 1
        print("Delete the object with id: ", self.id)


print(Bug.__doc__)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])


bugs[32].__del__()
bugs[23].__del__()

print("Last object id: ", bugs[-1].id)

print("Number of objects", Bug.counter)

time.sleep(10)