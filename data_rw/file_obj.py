# FILE R/W VIA OBJECT
class FILE:
    def __init__(self, name):
        self.name = name
        self.file = None # haven't open the file
    def open(self):
        self.file = open(self.name, mode = "r+", encoding = "utf-8")
    def read(self):
        return self.file.read()
    def close(self):
        self.file.close

f1 = FILE("data/data3.txt")
f1.open()
data = f1.read()
f1.close()
print(data)

f2 = FILE("data/data4.txt")
f2.open()
data = f2.read()
f2.close()
print(data)

