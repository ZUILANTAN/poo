class point():
    def move (self,x,y):
        self.x = x
        self.y = y
    def origin(self):
        self.x = 0
        self.y = 0
p1 = point()
p2 = point()
print(p1,p2)
p1.move(7,5)
p2.move(4,6)
print(p1.x,p1.y)
print(p2.y,p2.x)

#ejercicio
#crear un metodo que devuelva el punto al origen

p1.origin()
p2.origin()

print(p1.x,p1.y)
print(p2.y,p2.x)
